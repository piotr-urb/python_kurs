
filename = "tekst.txt"
with open(filename) as f:
    content = f.read()
    content = content.split()
    print(content)
for word in content:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word is :")

