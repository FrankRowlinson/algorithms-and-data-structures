from priority_queue import PriorityQueue
from functools import total_ordering
from sys import stdin, stdout


@total_ordering
class Processor:
    __id = -1
    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        self.n = self.__id
        self.priority = 0

    def __eq__(self, other):
        return (-self.priority, -self.n) == (-other.priority, -other.n)
    
    def __gt__(self, other):
        return (-self.priority, -self.n) > (-other.priority, -other.n)


class ProcessorQueue(PriorityQueue):
    def __init__(self, n=100):
        self.__length = n
        self.__size = n
        self.__heap = [Processor() for _ in range(n)]

    def insert(self, el) -> None:
        self.__heap[-1] = el
        self.__size += 1
        n = self.__size
        k = n - 1
        self._siftup(self.__heap, k)
    
    def extract_max(self) -> int:
        x = self.__size - self.__length - 1
        self.__heap[0], self.__heap[x] = self.__heap[x], self.__heap[0]
        max_el = self.__heap[x]
        self.__size -= 1
        n = self.__size
        k = 0
        self._siftdown(self.__heap, k, n)
        return max_el


n, m = map(int, stdin.readline().strip().split())
tasks = map(int, stdin.readline().strip().split())
heap = ProcessorQueue(n)
for task in tasks:
    processor = heap.extract_max()
    stdout.write(f"{processor.n} {processor.priority}\n")
    processor.priority += task
    heap.insert(processor)
