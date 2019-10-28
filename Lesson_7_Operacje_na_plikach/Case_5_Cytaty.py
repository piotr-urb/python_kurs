
filename = input("Your file:")
with open(filename) as f:
    list_of_words = f.read()
    print(list_of_words)
    list_of_words = list_of_words.strip(',')
    list_of_words = list_of_words.split(" ")


for n in range(len(list_of_words)):
    if len(list_of_words[n]) > len(list_of_words[n+1]):
        longest = list_of_words[n]
        print(longest)
    elif len(list_of_words[n]) < len(list_of_words[n+1]):
        longest = list_of_words[n+1]
        print(longest)
    else:
        longest = list_of_words[n+1]
        print(longest)
print(longest)
