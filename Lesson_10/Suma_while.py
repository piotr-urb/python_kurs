
def sum(n):
    s = 0
    for a in range(1, n+):
        s = s + a
    return s
print("Suma petla for:", sum(10))


def sum_while(n):
    s=0
    while n>0:
        s=s+n
        n=n-1
    return s
print("Suma while", sum_while(10))


def sum_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursion(n-1)
print("Suma rekurencyjnie:", sum_recursion(10))