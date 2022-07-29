# implementation of a data structure called 'priority queue'
# a queue where next extracted object is one with the highest priority
# second version, because first one sucks
# tried to match user experience to previous implementation but rework internal logic entirely


class PriorityQueue:
    def __init__(self):
        self.__heap = list()
        self.__length = 0

    @classmethod
    def heapify(cls, array: list) -> None:
        n = len(array)
        for k in range((n >> 1) - 1, -1, -1):
            cls.__siftdown(array, k, n)

    def __siftdown(self, array: list, k: int, n: int) -> None:
        max_index = n - 1
        while True:
            if k >= max_index:
                break
            left = k * 2 + 1 if k * 2 + 1 <= max_index else k
            right = k * 2 + 2 if k * 2 + 2 <= max_index else k
            if array[k] == max(array[k], array[right], array[left]):
                return
            if array[left] > array[right]:
                array[k], array[left] = array[left], array[k]
                k = left
            else:
                array[k], array[right] = array[right], array[k]
                k = right

    def __siftup(self, array: list, k: int) -> None:
        while True:
            if k == 0:
                break
            parent = (k - 1) >> 1
            if array[k] > array[parent]:
                array[k], array[parent] = array[parent], array[k]
                k = parent
            else:
                return
    
    def insert(self, el) -> None:
        self.__heap.append(el)
        self.__length += 1
        n = self.__length
        k = n - 1
        self.__siftup(self.__heap, k)
    
    def extract_max(self) -> int:
        self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]
        max_el = self.__heap.pop()
        self.__length -= 1
        n = self.__length
        k = 0
        self.__siftdown(self.__heap, k, n)
        return max_el
    
    def __bool__(self):
        return bool(self.__length)


pq = PriorityQueue()
array = [1, 3, 4, 5, 5, 1, 3, 4, 5, 6, 6, 7]
[pq.insert(i) for i in array]
while pq:
    print(pq.extract_max())

        