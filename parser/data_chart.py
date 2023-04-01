import os
import matplotlib.pyplot as plt

# Get the path of the directory where the program is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Prompt the user to enter the filename
filename = input("Enter the name of the file: ")
file_path = os.path.join(dir_path, filename)

# Check if the file exists
if not os.path.exists(file_path):
    print("Error: file not found.")
    exit()

# Read the contents of the file
with open(file_path, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    if num_lines == 0:
        print("Error: file is empty.")
        exit()

# Prompt the user to enter the starting and ending lines
start_line = int(input(f"Enter the starting line number (1 to {num_lines}): "))
end_line = int(input(f"Enter the ending line number ({start_line} to {num_lines}): "))

# Check if the line numbers are valid
if start_line < 1 or end_line > num_lines or start_line > end_line:
    print("Error: invalid line numbers.")
    exit()

# Extract the data from the selected lines
data = []
for i in range(start_line - 1, end_line):
    data.append(float(lines[i]))

# Plot the chart
plt.plot(data)
plt.xlabel('Sample number')
plt.ylabel('Value')
plt.title('Selected Data')
plt.show()
