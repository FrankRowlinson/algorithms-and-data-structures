# sort an array using insertion sort algorithm
# sorts given array in place (i.e. don't use any additional memory)
# speed: O(n^2)
from random import randint


def insertion_sort(array: list) -> None:
    n = len(array)
    # if array contains 1 or 0 elements, 'for' loop won't start    
    for i in range(1, n):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            # if in 2 neighbouring elements left is higher than right, swap them
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def test():
    for _ in range(10):
        array = [randint(0, 10 ** 3) for _ in range(10 ** 3)]
        array_sorted = sorted(array) # create a sorted copy of an array using built-in function 'sorted'
        insertion_sort(array) # sort original array
        assert array == array_sorted, "sorted incorrectly"
    

if __name__ == '__main__':
    test()        
    