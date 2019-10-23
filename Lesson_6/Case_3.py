# maximum_of (A,b,c)
def max_of_2(first, second):
    return first if first > second else second

def maximum_of(a, b, c):
    return max_of_2 (max_of_2(a, b), c)
def read_value():
    return int(input("Put integer value:"))
# max_ab = a if a>b else b
# max_abc = max_ab if max_ab > c else c
#    if a>b
#       max_ab = a
#   else :
#       max_ab = b
#    if max_ab > c :
#        max_abc = max_ab
#   else :
#        max_abc = c
#   return max_abc
x = read_value()
y = read_value()
z = read_value()
result = maximum_of(x,y,z)
print("Max value: ", result)