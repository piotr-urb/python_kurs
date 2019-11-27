def timer():
    def sort_elements():
        start = time.now()
        sort_metod()
        end = time.now()
        return end - start
    return sort_elements
@timer
def quicksort():
    pass
@timer
def counttingsort():
    pass
@timer
def bubblesort():
    pass
# start = time.now()
# quicksort(Lista_10000_elementów)
# end = time.now()
clock = timer()
buble = timer()
counting = timer()
result


