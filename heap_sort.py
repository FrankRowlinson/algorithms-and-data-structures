import priority_queue as pq
from random import randint as rand
from timeit import repeat
import heapq


def heap_sort(array):
    heap = pq.PriorityQueue()
    [heap.insert(i) for i in array]
    while heap:
        array.append(heap.extract_max())
    
def heapq_sort(array):
    heap = []
    for el in array:
        heapq.heappush(heap, el)
    return [heapq.heappop(heap) for i in range(len(array))]

def test_heap_sort():
    array = [rand(0, 10 ** 4) for _ in range(10 ** 3)]
    heap_sort(array)

def test_heapq_sort():
    array = [rand(0, 10 ** 4) for _ in range(10 ** 3)]
    heapq_sort(array)


def main():
    print("testing heapq sort...")
    print(*repeat(test_heapq_sort, repeat=5, number=100), sep='\n')
    print("done! times above correspond to heapq tests")
    print("now let's test heap sort using my own implementation of heap")
    print(*repeat(test_heap_sort, repeat=5, number=100), sep='\n')
    print("done!")


if __name__ == '__main__':
    main()

# conclusion: my implementation of heap sucks c: