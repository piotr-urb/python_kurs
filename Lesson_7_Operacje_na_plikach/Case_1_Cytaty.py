
import random

filename = 'Cytaty.txt'
with open(filename) as f:
    list = f.readlines()
list_for_today = random.choice(list).strip()
print("List of the day ")
print('*'*100)
print(list_for_today.center(100))
print('*'*100)