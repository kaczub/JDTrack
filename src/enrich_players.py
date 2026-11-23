#!/usr/bin/env python3
"""Uzupełnia liczbę graczy w src/songs.json na podstawie Just Dance Wiki.

Dla piosenek bez pola `players` pyta Fandom o infobox (`|mode = Solo/Duet/...`).
Wymaga internetu. Użycie: python3 src/enrich_players.py
"""
import json
import pathlib
import re
import time
import unicodedata
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SONGS = ROOT / "src" / "songs.json"
API = "https://justdance.fandom.com/api.php"
UA = {"User-Agent": "Mozilla/5.0 (Just Dance party planner)"}
MODE = {"solo": 1, "duet": 2, "trio": 3, "quartet": 4, "dance crew": 4, "dance crew 4": 4}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def api(params: dict) -> dict:
    params = {**params, "format": "json", "formatversion": "2"}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=30))


def parse_mode(content: str):
    m = re.search(r"\|\s*mode\s*=\s*([^\n|]+)", content)
    if not m:
        return None
    raw = m.group(1)
    raw = re.sub(r"<ref.*", "", raw, flags=re.S)
    raw = raw.replace("[[", "").replace("]]", "").replace("{{", "").replace("}}", "")
    raw = re.sub(r"<br\s*/?>", " / ", raw)
    raw = re.split(r"[/\n]", raw)[0]
    raw = re.sub(r"[^A-Za-z ]", " ", raw)
    raw = re.sub(r"\s+", " ", raw).strip().lower()
    for key, val in MODE.items():
        if raw.startswith(key):
            return val
    return None


def fetch_exact(titles):
    out = {}
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        data = api({
            "action": "query",
            "prop": "revisions",
            "rvprop": "content",
            "titles": "|".join(chunk),
            "redirects": "1",
        })
        for page in data.get("query", {}).get("pages", []):
            if page.get("missing"):
                continue
            content = (page.get("revisions") or [{}])[0].get("content", "")
            mode = parse_mode(content)
            if mode:
                out[page["title"]] = (mode, content)
    return out


def search_title(title):
    data = api({
        "action": "query",
        "list": "search",
        "srsearch": title,
        "srlimit": "3",
    })
    return [x["title"] for x in data.get("query", {}).get("search", [])]


def main() -> None:
    songs = json.loads(SONGS.read_text(encoding="utf-8"))
    missing = [s for s in songs if not s.get("players")]
    print(f"Bez liczby graczy: {len(missing)}")

    # 1) dokładne tytuły
    exact = fetch_exact([s["title"] for s in missing])
    print(f"Trafienia po tytule: {len(exact)}")

    # 2) dopasowanie po znormalizowanym tytule
    by_norm = {}
    for page_title, (mode, _) in exact.items():
        by_norm.setdefault(norm(page_title), (mode, page_title))

    unresolved = []
    for s in missing:
        hit = by_norm.get(norm(s["title"]))
        if hit:
            s["players"] = hit[0]
        else:
            unresolved.append(s)

    # 3) szukanie po frazie
    print(f"Do wyszukania: {len(unresolved)}")
    for idx, s in enumerate(unresolved, 1):
        if s.get("players"):
            continue
        try:
            titles = search_title(s["title"])
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {s['title']}: {exc}")
            continue
        for t in titles:
            if norm(t) != norm(s["title"]):
                continue
            found = fetch_exact([t])
            if t in found or found:
                mode = list(found.values())[0][0]
                s["players"] = mode
                break
        if idx % 20 == 0:
            print(f"  ... {idx}/{len(unresolved)}")
        time.sleep(0.2)

    SONGS.write_text(json.dumps(songs, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    from collections import Counter
    print("Liczba graczy:", Counter(s.get("players") for s in songs))
    still = [s for s in songs if not s.get("players")]
    print(f"Bez danych: {len(still)}")
    for s in still:
        print("  -", s["game"], s["title"])


if __name__ == "__main__":
    main()
