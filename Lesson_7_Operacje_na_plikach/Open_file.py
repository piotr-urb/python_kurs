filename = 'tekst.txt'

with open(filename, 'r') as f:
    content = f.read()
    print(content)
print("Koniec")

f = open(filename)
print()