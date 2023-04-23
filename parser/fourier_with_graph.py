import re
import numpy as np
import matplotlib.pyplot as plt

# Odczyt z pliku
filename = input("Wpisz nazwę zdekodowanego pliku r3a: ")
with open(filename, 'r') as file:
    data = file.readlines()

# Przetwórz dane na liczby złożone
data = [complex(re.sub(r'[^\d+\-j.]', '', d)) for d in data]

# Szybka transformata fouriera
fft = np.fft.fft(data)

# Wylicz zakresy
mag = np.abs(fft)

# Wyrysuj pierwszą połowę zakresu (ze względu na to że druga połowa stanowi lustrzane odbicie)
N = len(mag)
plt.plot(mag[:N // 2])

# limit połowy zakresu
plt.xlim(0, N // 2)

# Podpisy
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT Magnitude Plot')

# Wyświetlanie wykresu
plt.show()
