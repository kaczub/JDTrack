#!/usr/bin/env python3
"""Buduje index.html z src/template.html + src/songs.json.

Użycie:  python3 src/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

GAMES = [
    {"id": "JD1",    "short": "JD 1",    "full": "Just Dance",      "year": 2009, "color": "#ff6b9d"},
    {"id": "JD2",    "short": "JD 2",    "full": "Just Dance 2",    "year": 2010, "color": "#ffa94d"},
    {"id": "JD3",    "short": "JD 3",    "full": "Just Dance 3",    "year": 2011, "color": "#ffd43b"},
    {"id": "JD4",    "short": "JD 4",    "full": "Just Dance 4",    "year": 2012, "color": "#a9e34b"},
    {"id": "JD2014", "short": "JD 2014", "full": "Just Dance 2014", "year": 2013, "color": "#51cf66"},
    {"id": "JD2015", "short": "JD 2015", "full": "Just Dance 2015", "year": 2014, "color": "#38d9a9"},
    {"id": "JD2016", "short": "JD 2016", "full": "Just Dance 2016", "year": 2015, "color": "#22b8cf"},
    {"id": "JD2017", "short": "JD 2017", "full": "Just Dance 2017", "year": 2016, "color": "#4dabf7"},
    {"id": "JD2018", "short": "JD 2018", "full": "Just Dance 2018", "year": 2017, "color": "#9775fa"},
    {"id": "JD2019", "short": "JD 2019", "full": "Just Dance 2019", "year": 2018, "color": "#f06595"},
    {"id": "JD2020", "short": "JD 2020", "full": "Just Dance 2020", "year": 2019, "color": "#ff922b"},
]


def main() -> None:
    songs = json.loads((SRC / "songs.json").read_text(encoding="utf-8"))
    template = (SRC / "template.html").read_text(encoding="utf-8")
    theme = (SRC / "theme.css").read_text(encoding="utf-8")
    template = template.replace("__CSS__", theme)
    template = template.replace(
        "__GAMES_JSON__",
        json.dumps(GAMES, ensure_ascii=False, separators=(",", ":")),
    )
    template = template.replace(
        "__SONGS_JSON__",
        json.dumps(songs, ensure_ascii=False, separators=(",", ":")),
    )
    (ROOT / "index.html").write_text(template, encoding="utf-8")
    print(f"index.html: {len(template):,} bytes, {len(songs)} songs")


if __name__ == "__main__":
    main()
