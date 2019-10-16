people = [1, 2, 3, (10,20), 4,5]
print(people)
a=0

for a in range(len(people)):
    if isinstance(people, tuple):
        a = a + 1
        break
        print(people[a])





