filename = 'tekst.txt'
with open(filename) as fopen:
    list_of_lines = fopen.readlines()
# - operuje już tylko na zwykłaej liscie- ##
print(list_of_lines)
print("-------------------------")

for i in range(len(list_of_lines)):
    print(f"Linia{i}:", list_of_lines[i].strip('\n'), end="*")