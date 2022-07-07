# implementation of a concept called 'priority queue'
# a queue where next extractable object is one with the highest priority

# storing priorities of queue via Nodes because then I can just modify values and not actually swap objects
# and because I like using classes for everything :D
import sys


class Node:
    __slots__ = 'value',

    def __init__(self, value: int) -> None:
        self.value = value

    def __setattr__(self, __name: str, __value: int) -> None:
        if not isinstance(__value, int):
            raise TypeError("Priority can only be represented by type int")
        object.__setattr__(self, __name, __value)


class PriorityQueue:
    def __init__(self) -> None:
        self.__queue = list()

    # extract max by swapping values of root and last leaf, popping last leaf and sifting down
    def extract_max(self) -> Node or None:
        if len(self.__queue) == 0:
            return
        if len(self.__queue) > 1:
            self.__queue[0].value, self.__queue[-1].value = self.__queue[-1].value, self.__queue[0].value
        max_priority = self.__queue.pop().value
        self.sift_down()
        return max_priority
    
    # insert at the end of the heap and sift up
    def insert(self, x: int) -> None:
        self.__queue.append(Node(x))
        self.sift_up()

    # sift up last leaf of the tree (heap)
    def sift_up(self) -> None:
        current_index = len(self.__queue) - 1
        while current_index != 0:
            parent_index = (current_index + 1) // 2 - 1
            if self.__queue[current_index].value > self.__queue[parent_index].value:
                self.__queue[current_index], self.__queue[parent_index] = self.__queue[parent_index], self.__queue[current_index]
                current_index = parent_index
            else:
                break

    def __swap_with_child(self, child_index: int, current_index: int) -> int or None:
        if self.__queue[child_index].value > self.__queue[current_index].value:
            self.__queue[child_index].value, self.__queue[current_index].value = \
                self.__queue[current_index].value, self.__queue[child_index].value
            return child_index
        return None

    # sift down root of the tree (heap)     
    def sift_down(self) -> None:
        length = len(self.__queue)
        current_index = 0
        while (current_index + 1) * 2 <= length:
            # if our node has only 1 child...
            if (current_index + 1) * 2 + 1 > length:
                child_index = (current_index + 1) * 2 - 1
                # if child's priority is higher, swap
                current_index = self.__swap_with_child(child_index, current_index)
                if current_index is None:
                    break
            # ...or it has 2 children      
            else:
                left_child_index = (current_index + 1) * 2 - 1
                right_child_index = (current_index + 1) * 2
                if self.__queue[left_child_index].value > self.__queue[right_child_index].value:
                    child_index = left_child_index
                else:
                    child_index = right_child_index
                current_index = self.__swap_with_child(child_index, current_index)
                if current_index is None:
                    break
    
    def __call__(self, function: str) -> None or int:
        if function.split()[0] not in ('ExtractMax', 'Insert'):
            raise ValueError(f"'{function}' doesn't match the supported function type")
        if function == 'ExtractMax':
            max_priority = self.extract_max()
            print(max_priority)
            return max_priority
        new_priority = int(function.split()[1])
        self.insert(new_priority)


def main():
    n = int(input())
    heap = PriorityQueue()
    for _ in range(n):
        # using sys.stdin.readline() here, because on high-loaded tests it performs better than input()
        line = sys.stdin.readline().strip()
        heap(line)
        
    
if __name__ == '__main__':
    main()
                
            