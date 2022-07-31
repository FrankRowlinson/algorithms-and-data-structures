# this algorithm returns editing distance from char sequence A to char sequence B, i.e. how many 
# editing actions are required to transform A to B. 
# by editing actions we mean delete, insert and replace.
# editing is happening at 1 cell/index of a data array or char sequence at a time.
# example: 'ABCD' -> 'BCDEF' editing distance here equals to 3. 
# we need to delete 'A' and insert 'E' and 'F'
# algorithm works using dynamic programming principles
from math import inf


# A and B are data sets. i and j are end indices of those data sets that we are currently working 
# with. D is memo table to collect every solution so we don't count something twice
def editing_distance_td(A: list or str, 
                        B: list or str, 
                        i: int=None, 
                        j: int=None, 
                        D: list=None) -> int:
    n = len(A)
    m = len(B)
    if D is None:
        # initialize two-dimensional array with default values being infinity
        D = [[inf for _ in range(m + 1)] for _ in range(n + 1)]
    if i is None:
        i = n
        j = m
    if D[i][j] != inf:
        return D[i][j]
    if i == 0:
        D[i][j] = j
    elif j == 0:
        D[i][j] = i
    else:
        ins = editing_distance_td(A, B, i, j - 1, D) + 1
        delete = editing_distance_td(A, B, i - 1, j, D) + 1
        sub = editing_distance_td(A, B, i - 1, j - 1, D) + (A[i - 1] != B[j - 1])
        D[i][j] = min(ins, delete, sub)
    return D[i][j]


print(editing_distance_td('distance', 'editing')) # == 5