print("Podaj swoją wagę")
weight = float(input())
print("Podaj swój wzrost")
hight = float(input())
bmi = " Nie zdefiniowano"
try:
    bmi = weight/hight*hight
except ZeroDivisionError as e:
    print("Pamiętaj nie dziel przez zero, wzrost nie może być zerem",e)
print(bmi)