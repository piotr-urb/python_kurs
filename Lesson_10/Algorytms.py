#E- mail
mail = input("Podaj szykany e-mail:")
mail_list = ["tomasz.nowak@wp.pl", "konrad.stan@allegro.pl"]
if mail.find('@') == -1:
    print(" E- mail should have an '@'")
    try:
        mail_list.index(mail)
        print("E-mail is on the list")
    except ValueError:
        print("E-mail not found ")

#if mail in mail_list:
#   print(" Znalazłem szukany e-mail:")