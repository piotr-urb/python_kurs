print("Palindrom")
p = "kajak"
show = input("Wprowadz zdanie: ")
sen = show
sen = sen.replace(" ","")
sen.lower()
a = show
b = sen[::-1]
print("1:", a)
print("2:", sen)
print("3:", b)
print("4:", a == b)


