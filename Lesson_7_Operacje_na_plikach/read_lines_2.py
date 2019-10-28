with open('tekst.txt', 'r') as fopen:
    lines = fopen.readlines()
    print(lines)

for l in range(len(lines)):
    print("Line " + str(l), lines[l])