def print_segment(n):
    for size in range(1, n+1, 2):
        print((size * "*").center(n))

print_segment(10)