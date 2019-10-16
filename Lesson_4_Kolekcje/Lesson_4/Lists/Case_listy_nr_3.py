counter = int(input("Ile elementów chcesz dodać?" ))
elements=[]
for a in range(counter) :
    tmp = input(" podaj dowolny ciąg znaków:")
    elements.append(tmp)
print(elements)
print(" Czy pierwszy i ostani element są takie same:", elements[0] == elements[-1])
if elements[0] == elements[-1]:
    print("Pierwszy i ostatni element są takie same")
else:
    print("Elementy nie są takie same")

    #------------------- dodatkowe kody--------------------------
elements2 = []
counter2 = 5
    while (counter2 > 0):
  elements2.append(tmp)
   counter2 -=1
print(elements2)
#-----------while example----------
num_arr = []
while True:
    tmp = input("Podaj nowy element.Naciśnij Q żeby zakończyć")
    if tmp == "Q":
        num_arr.append(tmp)
print(num_arr)



