# function to check whether or not sequence of brackets is balanced, 
# i.e. they're opened and closed correctly
# implemented using self-made stack structure
# input format: sequence of brackets without any other symbols and spaces
# returns bool


class EmptyPopException(Exception):
    pass


class StackObj:
    def __init__(self, value):
        self.value = value
        self.prev = None

    def __bool__(self):
        return bool(self.value)


class Stack:
    def __init__(self):
        self.__top = None

    def push(self, obj):
        obj = StackObj(obj)
        obj.prev = self.__top
        self.__top = obj

    def pop(self):
        if not self.__top:
            raise EmptyPopException("Stack object is empty, there is nothing to pop")
        pop_element = self.__top
        self.__top = self.__top.prev
        return pop_element.value

    def __bool__(self):
        return bool(self.__top)

    @property
    def top(self):
        return self.__top.value if self.__top else None


def check_bracket_sequence(brackets: str) -> bool:
    stack = Stack()
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    for bracket in brackets:
        if bracket in brackets_dict:
            stack.push(bracket)
        elif stack and brackets_dict[stack.top] == bracket:
            stack.pop()
        else:
            return False
    return not stack


def main():
    while True:
        seq = input()
        if not seq:
            break
        print(check_bracket_sequence(seq))


if __name__ == "__main__":
    main()
