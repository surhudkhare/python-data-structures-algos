from abc import ABC, abstractmethod
class Stack(ABC):
    """A linear data structure which follows LIFO
    Can be implemented using 1) in-built list, 2) deque from collections, 3) Linked List
    We will use this as an abstract class  to build all 3 implementations
    """
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class StackList(Stack):
    """Implementation using python in-built list"""
    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self) -> str:
        return str(self.stack)
    
s = StackList()
s.push(3)
print(s.peek())
print(s)
s.push(4)
print(s.peek())
print(s)
s.pop()
print(s.peek())
print(s)