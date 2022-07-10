# this algorithm not only sorts an array by merge, but also counts exact amount of inversions inside
# has to be launched separately with each array though because I use global variable (lazy)

from collections import deque


def merge_sort(array: list, l: int=0, r: int=None) -> list:
    if not r:
        r = len(array)
    if len(array[l:r]) > 1:
        m = (l + r) >> 1    
        return merge(merge_sort(array, l, m), merge_sort(array, m, r))
    else:
        return array[l:r]

def merge(l_half: list, r_half: list) -> list:
    global inversions
    result = list()
    l_i = 0
    r_i = 0
    l_bound = len(l_half)
    r_bound = len(r_half)
    while l_bound > l_i and r_bound > r_i:
        if r_half[r_i] < l_half[l_i]:
            inversions += (l_bound - l_i)
            result.append(r_half[r_i])
            r_i += 1
        else:
            result.append(l_half[l_i])
            l_i += 1
    result.extend(r_half[r_i:] + l_half[l_i:])
    return result


inversions = 0
arr = list(map(int, input().split()))
merged = merge_sort(arr)
print(inversions)