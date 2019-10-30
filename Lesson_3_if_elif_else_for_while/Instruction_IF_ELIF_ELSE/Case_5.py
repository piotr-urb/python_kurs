print(" Wpisz hasło. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków")
password = input("Put the password:")
good_password = "my_password_6"
print(password)
print(len(password))
if password == good_password :
    print(" This password is good")
elif len(password) >= len(good_password):
    print("Your password is too short")
elif len(password) <= len(good_password):
    print("Your password is too long")
else :
    print(" This password is incorrect ")

