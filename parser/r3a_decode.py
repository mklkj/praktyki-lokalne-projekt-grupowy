import os
import struct

# Get the path of the directory where the program is located
dir_path = os.path.dirname(os.path.realpath(__file__))

selected_file = input("Enter the file name (without .r3a extension): ")

with open(os.path.join(dir_path, selected_file + ".r3a"), "rb") as source:
    with open(os.path.join(dir_path, "output-" + os.path.basename(selected_file) + ".txt"), "w") as output:
        max_val = float("-inf")
        min_val = float("inf")
        i = 0
        head_only = False
        while True:
            x = source.read(2)
            if not x:
                break
            x = struct.unpack('h', x)[0]
            if max_val < x:
                max_val = x
            if min_val > x:
                min_val = x
            if i == 10000 and head_only:
                break
            i += 1
            output.write(str(x >> 2) + "\n")

print("Samples count: ", i)
print("MAX: ", max_val >> 2)
print("MIN: ", min_val >> 2)
