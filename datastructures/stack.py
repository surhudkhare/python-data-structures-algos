from abc import ABC, abstractmethod
from collections import deque
from datastructures.linked_list import LinkedList

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
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self) -> str:
        return str(self.stack)

class StackDeque(Stack):
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self) -> str:
        return str(self.stack)    


class StackLinkedList(Stack):
    def __init__(self) -> None:
        self.stack = LinkedList()

    def push(self, data):
        self.stack.insert(data)

    def pop(self):
        pop_element = self.stack.delete()
        return pop_element.data

    def peek(self):
        return self.stack.head.data

    def is_empty(self):
        return self.stack.size() == 0
    
    def __str__(self) -> str:
        return str(self.stack)

if __name__ == "__main__":
    sll = StackLinkedList()
    sll.push(3)
    sll.push(4)
    print(sll)