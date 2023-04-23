# Projekt lokalny — praktyki grupowe

- czyste dane
- 2 bajty to jest jedna liczba
- młodszy bajt jest pierwszy, starszy jest drugi
- konwertujemy na liczbę dziesiętną (dzielimy przez 4?????)
- zakodowane w U2, czyli wartość ujemna ma najstarszy bit....
- po zdekodowaniu dostaniemy całą serię liczb dziesiętnych

- odczyt co 5 milisekund, ale to nie ma nic do rzeczy (do kwestii odczytu danych)

## Big endian (starszy bajt na początku)

Odczytanie bajtów "tak jak są", hex
```sh
$ od -t x1 DATA-2022.08.25.16.56.50.777.r3a | head
0000000    e4  ff  10  00  f8  ff  04  00  e4  ff  14  00  f8  ff  08  00
```

Odczytanie bajtów "tak jak są", ale binarnie
```sh
$ xxd -b DATA-2022.08.25.16.56.50.777.r3a | head
00000000: 11100100 11111111 00010000 00000000 11111000 11111111
```


Odczytanie liczb "tak jak są", interpretując pierwszy bajt, jakby był tym starszym (big endian)
```sh
$ cat DATA-2022.08.25.16.56.50.777.r3a | dd conv=swab | od -d | head
0000000     58623    4096   63743    1024   58623    5120   63743    2048
```


## Little endian (młodszy bajt na początku)

Odczytanie liczb, zamieniając miejscami pierwszy bajt z drugim, biorąc najpierw drugi bajt jako starszy, pierwszy jako młodszy (little endian)
```sh
$ hexdump -d DATA-2022.08.25.16.56.50.777.r3a | head
0000000   65508   00016   65528   00004   65508   00020   65528   00008
```

## U2

65508 to w zapisie U2 będzie -28.

## Przesunięcie bitowe

Tak wyciągnięte dane są przesunięte o dwa bity w lewo, więc żeby uzyskać ostateczny wynik, trzeba przesunąć każdą liczbę 2 bity w prawo (to samo co dzielenie przez 4).

## Konwersja

1. Dane binarne
2. Hex
3. Hex, ale grupując po dwa bajty i w little endian
4. Konwersja na dziesiętną
5. Konwersja na dziesiętną, ale ze znakiem (U2 - kod uzupełnień do dwóch)
6. Przesunięcie bitowe w prawo o dwie pozycje — efektywnie dzielenie przez 4

`11100100 11111111` -> `e4 ff` --> `ffe4` --> `65508` --> `-28` --> `-7`

## Metadane

- Lodz-02_80-120MHz:
  - max = 37
  - min = -36
  - samples = 252_013_248
- Lodz-03_50-90MHz:
  - max = 29
  - min = -30
  - samples = 252_013_248
- Lodz-07_20-60MHz:
  - max = 113
  - min = -113
  - samples = 252_013_248

## Skrypty

```shell
$ python3 r3a_decode.py
Enter the file name (without .r3a extension): DATA-2022.10.25.11.47.52.509
$ python3 python3 binary_cutter.py
Podaj nazwę pliku: output-DATA-2022.10.25.11.47.52.509.txt
Podaj liczbę linii do odczytania: 16384
$ python3 fourier_with_graph.py                                                                                                      ✘ 1 master ✱
Wpisz nazwę zdekodowanego pliku r3a: short_test.txt
```
