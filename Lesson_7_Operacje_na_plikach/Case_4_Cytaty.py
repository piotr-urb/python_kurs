import random


def random_quote(words):
    list_for_today = random.choice(words).strip()
    return list_for_today.split(" - ")


def show(quote):
    print(list_for_today)
    print("List of the day ")
    print('*' * 100)
    print(quote[0].center(100))
    print(('~' + quote[1]).center(100))
    print('*' * 100)

filename = input("Your file:")
with open(filename) as f:
    list = f.readlines()
    for i in range(3):
        sentence = random_quote(list)
        print("-------------")
        show(sentence)

