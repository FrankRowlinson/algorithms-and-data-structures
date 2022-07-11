# quick sort algorithm. Works faster than merge sort
# sorts array in place
from random import choice, randint
import timeit

# split array into 2 parts, return middle point with index 'j'
# where all elements in the left part are less than or equal to A[j] and
# all elements in the right part are greater than A[j]
def partition(array: list, l: int, r: int) -> int:
    x = array[l]
    j = l
    for i in range(l + 1, r):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[l], array[j] = array[j], array[l]
    return j

# split array using partition and sort every part separately using same algorithm
def quick_sort(array: list, l: int=0, r: int=None) -> None:
    if r is None:
        r = len(array)
    if l >= r:
        return
    # mid = (l + r) >> 1
    # array[l], array[mid] = array[mid], array[l]
    m = partition(array, l, r)
    quick_sort(array, l, m)
    quick_sort(array, m + 1, r)


def test():
    array = [randint(0, 10 ** 4) for _ in range(10 ** 4)]
    array_sort_check = sorted(array) # sorted copy of an array to verify algorithm correctness
    quick_sort(array)
    assert array == array_sort_check, "quick sort failed"

def main():
    print(timeit.timeit(test, number=100))
        

if __name__ == '__main__':
    main()



