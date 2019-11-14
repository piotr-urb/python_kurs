import sys

def hello_exception():
    print('Początek programu')
    raise Exception('To jest ogólny wyjątek')
    print('Koniec programu')
try:
    hello_exception()
except ArithmeticError as ex:
    print("Oh nie, błąd:")
    print(sys.exc_info())
except:
    print(" Inny błąd")
    print(sys.exc_info())
#
#C:\Users\Piotr\AppData\Local\Programs\Python\Python37\pythonw.exe C:/Users/Piotr/Desktop/KURS_Python/Lesson_9_Exceptions/06_Raise.py
# Początek programu
# Traceback (most recent call last):
#   File "C:/Users/Piotr/Desktop/KURS_Python/Lesson_9_Exceptions/06_Raise.py", line 2, in <module>
#     raise Exception('To jest ogólny wyjątek')
# Exception: To jest ogólny wyjątek
#
# Process finished with exit code 1