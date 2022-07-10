# sort an array using merge sort algorithm
# creates sorted copy of an array (uses memory)

from random import randint
from collections import deque

# merge sort using recursion
def merge_sort(array: list, l: int=0, r: int=None) -> list:
    if not r:
        r = len(array)
    if len(array[l:r]) > 1:
        m = (l + r) >> 1    
        return merge(merge_sort(array, l, m), merge_sort(array, m, r))
    else:
        return array[l:r]

# iterative merge sort without recursion
def merge_sort_iterative(array: list) -> list:
    queue = deque([[i] for i in array])
    while len(queue) > 1:
        queue.append(merge(queue.popleft(), queue.popleft()))
    return queue.popleft()

# both algorithms above use this function. It's a basic logic behind merge sort
# it goes through 2 SORTED arrays and merge them element by element, comparing
def merge(l_half: list, r_half: list) -> list:
    result = list()
    l_i = 0
    r_i = 0
    l_bound = len(l_half)
    r_bound = len(r_half)
    while l_bound > l_i and r_bound > r_i:
        if r_half[r_i] > l_half[l_i]:
            result.append(l_half[l_i])
            l_i += 1
        else:
            result.append(r_half[r_i])
            r_i += 1    
    result.extend(r_half[r_i:] + l_half[l_i:])
    return result


def test():
    inversions = 0
    for _ in range(100):
        array = [randint(0, 10 ** 4) for _ in range(10 ** 4)]
        array_sort_check = sorted(array) # create a sorted copy of an array using built-in function 'sorted'
        # array_merge_sorted = merge_sort(array)
        array_merge_i_sorted = merge_sort_iterative(array)
        # assert array_merge_sorted == array_sort_check, "recursive merge sort failed"
        assert array_merge_i_sorted == array_sort_check, "iterative merge sort failed"
    

if __name__ == '__main__':
    test()
