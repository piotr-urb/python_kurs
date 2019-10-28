import random

filename = input("Your file:")
with open(filename) as f:
    list = f.readlines()

list_for_today = random.choice(list).strip()
list_for_today = list_for_today.split(" - ")
print(list_for_today)
print("List of the day ")
print('*'*100)
print(list_for_today[0].center(100))
print(('~' + list_for_today[1]).center(100))
print('*'*100)