
print("Podaj kilka liczb po przecinku:")
numbers = []
string = input()
print(string)
numbers = string.split(",")
print(numbers)
list_exc = []
for index, element in enumerate(numbers):
    print(index, ":", element)
    try:
        numbers[index] = float(element)
    except ValueError as er1:
        list_exc.append(er1)
        print("Wyjatek 1 ValueError", er1)
        numbers[index] = "-"
    except TypeError as er2:
        list_exc.append(er2)
        print("Wyjatek 2 ValueError", er2)
while "-" in numbers:
    numbers.remove("-")
print(numbers)

avg = sum(numbers)/len(numbers)
print(avg)
with open('save.txt', 'w') as f:
    f.write("Mamy błędy :)")
    for i in list_exc:
        f.write(str(i))

    #suma_1 = float(numbers[i])+float(numbers[i+1])
    #print(suma_1)
