import math


def read_first_lines(file_name, num_lines):
    # otwarcie pliku wejściowego i pliku wyjściowego
    with open(file_name, 'r') as f_in, open('short_test.txt', 'w') as f_out:
        # odczytanie pierwszych num_lines linii z pliku wejściowego i zapisanie ich do pliku wyjściowego
        for i in range(num_lines):
            line = f_in.readline()
            if not line:
                break
            f_out.write(line)


# przykładowe użycie funkcji read_first_lines
file_name = input("Podaj nazwę pliku: ")
num_lines = int(input("Podaj liczbę linii do odczytania: "))

# sprawdzenie, czy liczba linii jest potęgą liczby 2
if (num_lines & (num_lines - 1)) != 0:
    # jeśli nie, wyznaczenie najbliższej potęgi liczby 2
    lower_pow = 2 ** int(math.log(num_lines, 2))
    higher_pow = 2 ** int(math.log(num_lines, 2)) * 2
    print("Liczba linii musi być potęgą liczby 2. Najbliższe wartości to: {} i {}".format(lower_pow, higher_pow))
    num_lines = int(input("Podaj poprawną liczbę linii do odczytania: "))

read_first_lines(file_name, num_lines)
