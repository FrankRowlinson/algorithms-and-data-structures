# this function returns largest increasing subsequence from array
def lis_bottom_up(array: list) -> int:
    n = len(array)
    d = [0 for _ in range(n)]
    for i in range(n):
        d[i] = 1
        for j in range(0, i):
            if array[j] < array[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    answer = 0
    for i in range(n):
        answer = max(answer, d[i])
    lis = [0 for _ in range(answer)]
    k = 0
    for i in range(1, n):
        if d[i] > d[k]:
            k = i
    current_length = answer
    current_max = array[k]
    lis[current_length - 1] = current_max
    for i in range(k - 1, -1, -1):
        if array[i] < current_max and d[i] + 1 == current_length:
            current_length -= 1
            current_max = array[i]
            lis[current_length - 1] = current_max
    return lis


# this algorithm returns largest NON-increasing subsequence indexes of given array. O(n^2),
# should rewrite it to work with speed O(n*log(n))
def lnis_bottom_up(array: list) -> int:
    n = len(array)
    d = [0 for _ in range(n)]
    for i in range(n):
        d[i] = 1
        for j in range(0, i):
            if array[j] >= array[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    answer = 0
    for i in range(n):
        answer = max(answer, d[i])
    lnis = [0 for _ in range(answer)]
    k = 0
    for i in range(1, n):
        if d[i] > d[k]:
            k = i
    current_length = answer
    current_min = array[k]
    current_max_index = k
    lnis[current_length - 1] = current_max_index + 1
    for i in range(k - 1, -1, -1):
        if array[i] >= current_min and d[i] + 1 == current_length:
            current_length -= 1
            current_min = array[i]
            current_max_index = i
            lnis[current_length - 1] = current_max_index + 1
    return answer, lnis






    



