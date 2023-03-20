import matplotlib.pyplot as plt

x = []
y = []
i = 0
for line in open('output-Lodz-07_20-60MHz-signed.txt', 'r'):
    x.append(i)
    y.append(int(line))
    i += 1

plt.title("Students Marks")
plt.xlabel('Pomiar')
plt.ylabel('Wartość')
plt.yticks(y)
plt.plot(x, y, marker='o', c='g')

plt.show()
