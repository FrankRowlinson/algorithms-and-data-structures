# this algorithm works fast - O(n) - if input values are few unique numbers. Requires memory!
# e.g. [1, 2, 2, 2, 1, 1, 3, 3, 3, 2, 2, 1, 3, 2, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1, 3, 2, 1]
# in this implementation we'll assume that input array consists of numbers in [1..M] range and
# these numbers are continuous

def count_sort(array: list) -> list:
    m = max(array)
    n = len(array)
    B, result = [0 for _ in range(m)], [0 for _ in range(n)]
    for j in range(0, n):
        B[array[j] - 1] += 1
    for i in range(1, m):
        B[i] += B[i - 1]
    for j in range(n - 1, -1, -1):
        result[B[array[j] - 1] - 1] = array[j]
        B[array[j] - 1] -= 1
    return result


arr = [1, 2, 2, 2, 1, 1, 3, 3, 3, 2, 2, 1, 3, 2, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1, 3, 2, 1]
print(count_sort(arr))