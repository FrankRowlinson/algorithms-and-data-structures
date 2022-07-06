# algorithm dedicated to cover set of distinct segments with minimal number of dots
# where every segment should be covered by at least 1 dot

# receive number of segments and then segments themselves (a, b)
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
# sort by end of segment
segments.sort(key=lambda x: x[1])
dots = []
for segment in segments:
    # if dots list is currently empty or last dot in list not covering current segment, 
    # then add rightmost point of current segment into list
    if not dots or dots[-1] not in range(segment[0], segment[1] + 1):
        dots.append(segment[1])

# print results
print(len(dots))
print(*dots)