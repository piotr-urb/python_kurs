#Zadanie nr 4:
#4▹ Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#output:
#[4, 3, 2, 1]
#[14, 13, 12, 11]
#[24, 23, 22, 21]

input_num = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
a = len(input_num)
print(a)
new_list_1 = input_num[0: (a // 3)]
print(new_list_1)
new_list_2 = input_num[(a // 3): (2*a // 3)]
print(new_list_2)
new_list_3 = input_num[(a // 3)*2:]
print(new_list_3)
print('******************************')
print(new_list_1[4:: -1])
print(new_list_2[4:: -1])
print(new_list_3[4:: -1])
