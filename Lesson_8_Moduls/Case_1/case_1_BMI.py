
def calc_bmi(weight, height):
    return weight / (height ** 2)
def bmi_status(bmi):
    if bmi < 19:
        return "severly_underweight"
    elif bmi < 25:
        return "healthy"
    elif bmi < 30:
        return "overwieght"
    else:
        return "severly_overweight"


def main():
    h = 1.60
    w = 60
    print("88888888888888888888888")
    bmi = round(calc_bmi(w, h), 4)
    print(bmi_status(bmi))
if __name__ == "__main__":
    main()


