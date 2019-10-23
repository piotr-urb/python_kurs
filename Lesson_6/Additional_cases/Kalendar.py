


data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

a = 0
b = 13
print(data[a:b])
def my_list_number(numb):
    for c in range(1, 32):
        print("Kalendarz",c)
        c = c+1
        return numb

if str(data[0]) == "January":
    print("January")

#counter = int(input("Ile elementów chcesz dodać?" ))
#elements=[]
#for a in range(counter) :
#    tmp = input(" podaj dowolny ciąg znaków:")
#    elements.append(tmp)
#print(elements)