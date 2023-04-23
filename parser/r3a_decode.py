import os
import struct

# Get the path of the directory where the program is located
dir_path = os.path.dirname(os.path.realpath(__file__))

selected_file = input("Enter the file name (without .r3a extension): ")

with open(os.path.join(dir_path, selected_file + ".r3a"), "rb") as source:
    with open(os.path.join(dir_path, "output-" + os.path.basename(selected_file) + ".txt"), "w") as output:
        while True:
            x = source.read(2)
            if not x:
                break
            x = struct.unpack('h', x)[0]
            output.write(str(x >> 2) + "\n")
