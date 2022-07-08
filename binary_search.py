# algorithm to look for numbers in sorted array by using binary search
# task here is to receive an array of length n and find k numbers in it or return -1 if not found

def find(array: list, n: int) -> int:
    l = 0 # left and right boundaries
    r = len(array) - 1
    while l <= r:
        m = (l + r) >> 1 # bit shifting works exactly like integer division by 2, but faster
        if array[m] == n:
            return m + 1
        if array[m] > n:
            r = m - 1
        else:
            l = m + 1
    return -1


def main():
    n, *array = map(int, input().split())
    k, *numbers = map(int, input().split())
    for num in numbers:
        print(find(array, num), end=' ')


if __name__ == '__main__':
    main()