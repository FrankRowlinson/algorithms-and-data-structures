# this script transforms list into heap in place
# kinda the same thing as heapq.heapify(list)

def siftdown(array: list, k: int, n: int) -> int:
    global exchanges
    max_index = n - 1
    x = 0
    current_index = k
    while True:
        left = k * 2 + 1 if k * 2 + 1 <= max_index else k
        right = k * 2 + 2 if k * 2 + 2 <= max_index else k
        if array[k] == min(array[k], array[right], array[left]):
            return x
        if array[left] < array[right]:
            array[k], array[left] = array[left], array[k]
            exchanges.append((k, left))
            x += 1
            k = left
        else:
            array[k], array[right] = array[right], array[k]
            exchanges.append((k, right))
            x += 1
            k = right

exchanges = []
# number of elements in initial array (list)
n = int(input())
arr = list(map(int, input().split()))
# number of exchanges inside of array. Required for problem in course
m = 0
for k in range((n >> 1) - 1, -1, -1):
    m += siftdown(arr, k, n)
print(m)
for pair in exchanges:
    print(*pair)
