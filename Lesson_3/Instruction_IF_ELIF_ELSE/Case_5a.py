print(" Wpisz hasło. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków")
password = input("Put the password:")
good_password = "my_password_6"
alphanum = password.isalnum()
condition_only_lower = alphanum and password.islower()
if password == good_password :
    print("This password is good")
if len(password) <= 8:
    print("Your password is too short, Should be 8 chars")
if not alphanum:
    print("Your password should be alphanumeric")
if password.isalpha():
    print(" Should contain digits too ")
if password.isdigit():
    print(" Should contain letters too ")
if condition_only_lower:
    print(" Should contain at least 1 upper ")
print ("End")
