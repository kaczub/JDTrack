# Just Dance — stanowisko (Andrzejki)

Narzędzie do obsługi stanowiska z Just Dance na Wii: pełny katalog piosenek z 11 głównych części, kolejka drużyn, rekordy i wydruk. Wszystko w jednym pliku `index.html`, działa offline, bez internetu i bez instalacji.

## Szybki start

1. Otwórz `index.html` dwuklikiem (Chrome, Edge albo Safari).
2. Wejdź w **Ustawienia**:
   - wpisz nazwę imprezy,
   - ustaw slot (domyślnie 5 min),
   - zaznacz **gry na dziś** (np. JD 2019 + JD 2020).
3. W **Menu** ustaw filtr graczy (np. **4 os.**) i ewentualnie **pomijaj wrażliwe**, potem wyszukaj piosenkę i kliknij **＋ Kolejka**. Wpisz nazwę drużyny, **skład jako osobne osoby** (możesz dodać więcej niż 4) i wybierz jedną lub kilka piosenek — wszystkie trafią do kolejki.
4. W **Kolejce** kliknij **▶ Start** przy pierwszej drużynie. Po piosence: **Zakończ i wpisz wynik**.
5. **Rekordy** pokazują najlepszy wynik na każdej piosence, **Tablica** to duży widok na drugi ekran, a **Wydruk** daje menu/kolejkę/rekordy na papier.

Dane zapisują się w przeglądarce (localStorage). Możesz zamknąć kartę i wrócić — kolejka i rekordy zostaną.

## Co potrafi

- **494 piosenki** z 11 głównych części na Wii: Just Dance, 2, 3, 4, 2014–2020. Bez spin-offów typu Kids, Summer Party, Greatest Hits.
- Wyszukiwarka (ignoruje polskie znaki) i filtr po grze.
- **Filtr liczby graczy** — 1 / 2 / 3 / 4 osoby. Przy 4 pilotach ustaw „4 os.” i widzisz tylko utwory, które da się zagrać w pełnym składzie. Liczby pochodzą z Just Dance Wiki (1 utwór bez danych — pokazuje „? os.”).
- **Filtr „pomijaj wrażliwe”** — ukrywa utwory oznaczone jako wrażliwa choreografia. To subiektywna lista pomocnicza (twerking, mocno sugestywne ruchy), nie oficjalna klasyfikacja. Każdy utwór można oznaczyć lub odznaczyć przyciskiem **⚑** w Menu; lista jest w Ustawieniach.
- **Jasny / ciemny motyw** — monochromatyczny, bez kolorów. Przełącznik **◐** w nagłówku albo w Ustawieniach.
- **Gry na dziś** — katalog może mieć wszystkie wersje, ale menu i wydruk można zawęzić do tych, które są odpalone na konsoli.
- **Kolejka** drużyn: nazwa, **skład jako osobne osoby** (chipy przy występie), jedna lub kilka piosenek, start, timer, przesuwanie, usuwanie.
- **Wiele piosenek naraz** — w oknie dodawania zaznaczasz kilka utworów (✓), a aplikacja tworzy z nich osobne występy dla tej samej drużyny. Każdy dostaje własny wynik i rekord.
- **Czysty, statyczny interfejs** — bez animowanego tła i zbędnych efektów; liczy się kolejka i czytelność.
- **Rekordy per piosenka** — główna mechanika stanowiska: „pobij rekord tego utworu”. Osobno Top 10 wieczoru (traktuj je jako zabawę, bo różne piosenki mają różne maksimum punktowe).
- **Ostrzeżenie o zmianie gry** — jeśli w kolejce jest piosenka z innej wersji niż bieżąca, narzędzie pokaże „zmiana gry”. Dzięki temu widzisz, kiedy czeka Cię restart konsoli.
- **Wydruk**: menu piosenek (wg wersji albo wg liczby osób), kolejka, rekordy — wszystko na A4. Menu respektuje aktywne filtry (gra, liczba graczy, „wrażliwe”); w widoku wg wersji pokazuje liczbę osób, w widoku wg osób — grę.
- **Eksport CSV** (wyniki do Excela) i **kopia JSON** (backup całego stanu).
- Ukrywanie piosenek, których nie ma w Twoim ISO (np. regionalne dodatki).

## Zasady stanowiska, które się sprawdzają

- **4 piloty = maksymalnie 4 osoby.** Jedna piosenka na drużynę i zmiana — tak jest sprawiedliwie i nie blokuje kolejki.
- **Slot 5 minut** = ok. 3,5 min piosenki + 1,5 min na wynik i zmianę. To ok. 12 występów na godzinę.
- 30 graczy w składach po 4 osoby to ok. 8 kolejek, czyli ~40 minut, jeśli każdy zagra raz. Przez 3–4 godziny bez problemu obsłużysz wszystkich z powtórkami.
- **Dwie osoby obsługi:** host z mikrofonem (kolejka, zachęcanie, wyniki) i techniczny (piloty, konsola, awarie). Przy 70 osobach jedna osoba się nie wyrobi.
- **Rekordy zamiast eliminacji.** Przy stanowisku nie ma sensu turniej — ludzie podchodzą, kiedy chcą, a tablica rekordów daje rywalizację bez odpadania.
- **Host musi aktywnie zaczepiać.** Pasywna lista stoi pusta. Niech na start zagra ekipa techniczna i zbierze widownię.
- **Jedna wersja gry na blok.** Nie playlistuj przy otwartym stanowisku — ludzie wybierają z menu, a w obrębie jednej gry to kilka sekund. Zmianę wersji zaplanuj na przerwę, nie na każdą piosenkę.
- **Ustaw filtr „4 os.”** Katalog podaje liczbę graczy z Just Dance Wiki. Przy 4 pilotach najwięcej sensu mają utwory na 4 osoby, ale duety i sola też zagrają — wtedy część pilotów leży.

## Sprzęt, obraz i dźwięk

- **Obraz:** żółty chinch (composite) do projektora wystarczy — Just Dance nie ma drobnych detali. Ustaw proporcje (16:9 albo 4:3) i sprawdź overscan.
- **Dźwięk osobno:** czerwony/biały chinch z Wii przez przejściówkę 2×RCA → jack do szkolnego sound systemu albo aktywnych głośników. Wbudowany głośnik projektora nie nagłośni 70 osób.
- Jeśli dźwięk musi iść przez projektor, podłącz głośniki do jego wyjścia słuchawkowego/audio-out, nie licz na wbudowany głośnik.
- Weź przejściówkę **jack 3,5 mm → 6,3 mm** — szkolne wzmacniacze często mają duży jack.
- **Sensor bar** pod ekranem, w ustawieniach Wii „Below TV”. Konsola musi stać blisko tańczących (piloty łączą się po Bluetooth na ~8–10 m), więc to długi kabel wideo idzie do projektora, a nie konsola do tyłu sali.
- Włącz w projektorze **tryb gry / low latency** i zrób kalibrację w opcjach gry na docelowym sprzęcie.
- Ustaw konsolę na **60 Hz**, jeśli projektor przyjmuje; inaczej 50 Hz.
- **4 piloty + 2 zapasowe**, najlepiej z MotionPlus, numerowane, ze świeżymi bateriami i paskami. Weź chusteczki do przetarcia.
- **Test dzień wcześniej:** każda wersja z loadera, 4 piloty naraz, każda piosenka z menu, dźwięk i lag. To najważniejszy punkt.

Jeśli projektor ma tylko HDMI, a tor chinchowy nie zagra, tani konwerter **AV→HDMI** (~50 zł) załatwia sprawę. To nie to samo co Wii2HDMI.

## Wydruk

W zakładce **Wydruk** wybierz:

- **Menu: wersje** — lista pogrupowana po grach (przy każdej piosence liczba osób),
- **Menu: osoby** — lista pogrupowana po liczbie osób (1 / 2 / 3 / 4, przy piosence gra),
- **Kolejka** — aktualny występ + kolejka, z osobną kolumną składu,
- **Rekordy** — najlepsze wyniki per piosenka,
- **Wszystko** — menu wg wersji + kolejka + rekordy.

Nad kartką są **filtry wspólne z Menu** (liczba graczy, „pomijaj wrażliwe”) — podgląd odświeża się od razu po zmianie. Dopiero **Drukuj** otwiera okno druku. Drukuje się tylko biała kartka; interfejs jest ukrywany.

## Kopie zapasowe

- **Kopia JSON** w Ustawieniach — pełny stan (kolejka, wyniki, ustawienia).
- **Eksport CSV** w Rekordach — wyniki do Excela (średnik, UTF-8).
- **Wyczyść kolejkę** — usuwa występy, zostawia rekordy.
- **Wyczyść wszystko** — reset do stanu początkowego.

## Katalog — skąd i jakie są ograniczenia

Listy pochodzą z angielskiej Wikipedii (podstawowy soundtrack każdej gry). Katalog obejmuje 11 głównych części na Wii i **nie** zawiera spin-offów. Przy kilku grach mogą trafić się utwory regionalne, sklepowe lub DLC, których nie ma w Twoim ISO — użyj **✕** przy piosence, żeby ją ukryć (przywrócisz w Ustawieniach).

Liczba graczy pochodzi z Just Dance Wiki (infoboxy piosenek). Jeden utwór — „Crispy Duck” z pierwszej części — nie ma danych i pokazuje „? os.”.

Filtr „pomijaj wrażliwe” to **subiektywna lista pomocnicza**, a nie oficjalna klasyfikacja wiekowa. Startowa lista obejmuje utwory z mocno sugestywnymi ruchami (np. „Bum Bum Tam Tam”, „Side to Side”, „Blurred Lines”, „Taki Taki”). Oceniaj sam i zmieniaj listę przyciskiem **⚑** w Menu — to Ty odpowiadasz za dobór repertuaru.

Punktacja różnych piosenek nie jest w 100% porównywalna, dlatego rekordy liczone są osobno dla każdego utworu. Top 10 wieczoru to dodatek, nie oficjalny ranking.

## Przebudowa / edycja

- `index.html` — gotowa aplikacja (to ją otwierasz).
- `src/template.html` — szablon HTML + logika JS.
- `src/theme.css` — cały wygląd (minimal, czarno-biały).
- `src/songs.json` — katalog piosenek (liczba graczy + znaczniki „wrażliwe”).
- `src/build.py` — składa `index.html` z szablonu, stylów i katalogu.
- `src/enrich_players.py` — opcjonalnie dociąga liczbę graczy z Just Dance Wiki (wymaga internetu).

Po zmianach w `src/`:

```bash
python3 src/build.py
```
