# problem solution using disjoint sets data structure

import disjoint_sets
from sys import stdin, stdout


class DisjointTables(disjoint_sets.DisjointSets):
    def __init__(self, array: list, sizes: list) -> None:
        # number of elements in array. Can be increased in the future, so storing in variable
        self.__size = len(array)
        # create unique ids for each element in given array
        self.__ids = dict()
        for i, size in enumerate(sizes, start=1):
            self.__ids[i] = (i, size)
        # array with indices being those unique ids and values being parent ids. Initialize as
        # every element being it's own parent
        self.__parents = ['filler'] + [el for el in self.__ids]
        # array to store ranks of sets because it will save us time in union method
        self.__ranks = ['filler'] + [0 for _ in range(self.__size)]
        self.__max_size = max(sizes)

    def find(self, el) -> int:
        element_id = el
        if element_id != self.__parents[element_id]:
            self.__parents[element_id] = self.find(self.__parents[element_id])
        return self.__parents[element_id]

    # unite 2 sets by 2 of their elements
    def union(self, el1, el2) -> None:
        # i and j are ids of el1 and el2 sets respectively
        i = el1
        j = self.find(el2)
        if i == j:
            return
        i = self.find(el1)
        if self.__parents[i] != j:
            self.__parents[j] = i
            self.__ids[i] = (i, self.__ids[i][1] + self.__ids[j][1])
            self.__max_size = max(self.__max_size, self.__ids[i][1])
        

    def get_max_size(self):
        return self.__max_size
    


n, m = map(int, input().split())
sizes = list(map(int, stdin.readline().strip().split()))
sets = DisjointTables([f'table{i}' for i in range(n)], sizes)
for _ in range(m):
    destination, source = map(int, stdin.readline().strip().split())
    sets.union(destination, source)
    stdout.write(str(sets.get_max_size()) + "\n")

