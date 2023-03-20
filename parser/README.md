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


Odczytuje liczby "tak jak są", interpretując pierwszy bajt, jakby był tym starszym (big endian)
```sh
$ cat DATA-2022.08.25.16.56.50.777.r3a | dd conv=swab | od -d | head
0000000     58623    4096   63743    1024   58623    5120   63743    2048
```


## Little endian (młodszy bajt na początku)

Odczytuje liczby, zamieniając miejscami pierwszy bajt z drugim, biorąc najpierw drugi bajt jako starszy, pierwszy jako młodszy (little endian)
```sh
$ hexdump -d DATA-2022.08.25.16.56.50.777.r3a | head
0000000   65508   00016   65528   00004   65508   00020   65528   00008
```

## U2

65508 to -28 interpretując binarną liczbę jako będącą w zapisie U2


## Wyniki

- Lodz-02_80-120MHz:
  - signed: max=148, min=-144
- Lodz-03_50-90MHz:
  - signed: max=116, min=-120
- Lodz-07_20-60MHz:
  - signed: max=452, min=-452
