sum = 0
for a in range(1, 11):
    sum = sum + a
    if a == 10:
        print(sum)
    else:
        print(sum, end=" * ")
