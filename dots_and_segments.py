# this is challenge from algorithms course.
# there are n segments (a, b) and m dots.
# task is to show how many segments contain each dot in order of appearance
import sys

# partition method for quick sort
def quick_sort(array: list, l: int=0, r: int=None) -> None:
    if r is None:
        r = len(array)
    s = l
    e = r - 1
    mid = array[(s + e) >> 1]
    while s <= e:
        while array[s] < mid:
            s += 1
        while array[e] > mid:
            e -= 1
        if s <= e:
            s, e = e, s
            s += 1
            e -= 1
    if l < e:
        quick_sort(array, l, e)
    if r > s:
        quick_sort(array, s, r)
    
# binary search
def find_start(A: list, dot: int, n: int) -> int:
    l = 0
    r = n
    while l < r:
        m = (l + r) >> 1
        if A[m] <= dot:
            l = m + 1
        else:
            r = m
    return len(A[0:r])

def find_finish(B: list, dot: int, n: int) -> int:
    l = 0
    r = n
    while l < r:
        m = (l + r) >> 1
        if B[m] < dot:
            l = m + 1
        else:
            r = m
    return len(B[0:r])


def main():
    n, m = map(int, sys.stdin.readline().split())
    A, B = map(list, zip(*(list(map(int, sys.stdin.readline().split())) for _ in range(n))))
    dots = map(int, sys.stdin.readline().split())
    quick_sort(A)
    quick_sort(B)
    for dot in dots:
        N = find_start(A, dot, n)
        M = find_finish(B, dot, n)
        print(N - M, end=' ')


if __name__ == '__main__':
    main()

# right now it works, but works too slow. Doesn't pass tests. Need refactoring and better sorting algo