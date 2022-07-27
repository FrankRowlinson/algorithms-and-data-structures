# this is data structure called 'disjoint sets'
# given array at the beginning, it can separate any of it's elements to any number of disjoint sets
# (sets with no element in common)
# elements must be immutable and different!
# even though it's called 'sets', I don't use sets in this implementation :^)


class DisjointSets:
    def __init__(self, array: list) -> None:
        # number of elements in array. Can be increased in the future, so storing in variable
        self.__size = len(array)
        # create unique ids for each element in given array
        self.__ids = dict()
        for i, el in enumerate(array):
            self.__ids[el] = i
        # array with indices being those unique ids and values being parent ids. Initialize as
        # every element being it's own parent
        self.__parents = [self.__ids[el] for el in array]
        # array to store ranks of sets because it will save us time in union method
        self.__ranks = [0 for _ in range(self.__size)]
    
    # find id of the set in which the element is stored AND
    # relocate given and all in-between elements directly to root if possible
    # did with recursion, doesn't really matter, height of a tree not going to exceed 1000 in practice
    def find(self, el) -> int:
        element_id = self.__ids[el]
        if element_id != self.__parents[element_id]:
            self.__parents[element_id] = self.find(self.__parents[element_id])
        return self.__parents[element_id]

    # unite 2 sets by 2 of their elements
    def union(self, el1, el2) -> None:
        # i and j are ids of el1 and el2 sets respectively
        i = self.find(el1)
        j = self.find(el2)
        if i == j:
            return
        if self.__ranks[i] > self.__ranks[j]:
            self.__parents[j] = i
        else:
            self.__parents[i] = j
            if self.__ranks[i] == self.__ranks[j]:
                self.__ranks[j] += 1
    
    # these 2 are not necessary, just felt that it would be nice to be able to add elements after initialization
    def add_element(self, el) -> None:
        self.__ids[el] = self.__size
        self.__parents.append(self.__ids[el])
        self.__ranks.append(0)
        self.__size += 1

    def add_elements(self, elements) -> None:
        for el in elements:
            self.add_element(el)


sets = DisjointSets([1, 2, 4, 3, 6, 11, 7])
            