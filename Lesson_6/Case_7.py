def is_visa(is_card, number):
    if not is_card:
        return False
    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_master_card(is_card, number):
    if not is_card:
        return False
    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221,2721):
            return True


def is_american_express(is_card, number):
    if not is_card:
        return False
    if len(card_number) == 15:
        if card_number[0:2] in ("34", "37"):
            return True


card_number = input("Put the Card number here:")
can_be_card_number = False

if len(card_number) < 13 or len(card_number) > 16:
    print(" It is wrong number ")
else:
    if card_number.isdecimal():
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")

if is_visa(can_be_card_number, card_number):
    print("I'm Visa")
elif is_master_card(can_be_card_number, card_number):
    print("I'm MasterCard")
elif is_american_express(can_be_card_number, card_number):
    print("I'm American Express Card")
else:
    print("Not Known Card type")