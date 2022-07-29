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


heap = PriorityQueue()
n, m = map(int, stdin.readline().strip().split())
[heap.insert(Processor()) for _ in range(n)]
tasks = map(int, stdin.readline().strip().split())
for task in tasks:
    processor = heap.extract_max()
    stdout.write(f"{processor.n} {processor.priority}\n")
    processor.priority += task
    heap.insert(processor)
