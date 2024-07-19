from datastructures.stack import StackList, StackDeque, StackLinkedList
import pytest

class TestStackList:

    def test_initialization(self):
        stack = StackList()
        assert stack.is_empty() is True
        assert str(stack) == "[]"

    def test_push(self):
        stack = StackList()
        stack.push(1)
        assert stack.is_empty() is False
        assert str(stack) == "[1]"
        stack.push(2)
        assert str(stack) == "[1, 2]"

    def test_pop(self):
        stack = StackList()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert str(stack) == "[1]"
        stack.pop()
        assert stack.is_empty() is True

    def test_peek(self):
        stack = StackList()
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1

    def test_is_empty(self):
        stack = StackList()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False
        stack.pop()
        assert stack.is_empty() is True

    def test_str(self):
        stack = StackList()
        assert str(stack) == "[]"
        stack.push(1)
        assert str(stack) == "[1]"
        stack.push(2)
        assert str(stack) == "[1, 2]"
        stack.pop()
        assert str(stack) == "[1]"

class TestStackDeque:

    def test_initialization(self):
        stack = StackDeque()
        assert stack.is_empty()is True
        assert str(stack) == "deque([])"

    def test_push(self):
        stack = StackDeque()
        stack.push(1)
        assert stack.is_empty() is False
        assert str(stack) == "deque([1])"
        stack.push(2)
        assert str(stack) == "deque([1, 2])"

    def test_pop(self):
        stack = StackDeque()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert str(stack) == "deque([1])"
        stack.pop()
        assert stack.is_empty() is True

    def test_peek(self):
        stack = StackDeque()
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1

    def test_is_empty(self):
        stack = StackDeque()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False
        stack.pop()
        assert stack.is_empty() is True

    def test_str(self):
        stack = StackDeque()
        assert str(stack) == "deque([])"
        stack.push(1)
        assert str(stack) == "deque([1])"
        stack.push(2)
        assert str(stack) == "deque([1, 2])"
        stack.pop()
        assert str(stack) == "deque([1])"


# Test cases for StackLinkedList class
class TestStackLinkedList:

    def test_initialization(self):
        stack = StackLinkedList()
        assert stack.is_empty() is True

    def test_push(self):
        stack = StackLinkedList()
        stack.push(1)
        assert stack.is_empty() is False
        assert str(stack) == "1"
        stack.push(2)
        assert str(stack) == "2->1"

    def test_pop(self):
        stack = StackLinkedList()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert str(stack) == "1"
        assert stack.pop() == 1
        assert stack.is_empty() is True

    def test_peek(self):
        stack = StackLinkedList()
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1

    def test_is_empty(self):
        stack = StackLinkedList()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False
        stack.pop()
        assert stack.is_empty() is True

    def test_str(self):
        stack = StackLinkedList()
        assert str(stack) == 'Empty List'
        stack.push(1)
        assert str(stack) == "1"
        stack.push(2)
        assert str(stack) == "2->1"
        stack.pop()
        assert str(stack) == "1"

if __name__ == "__main__":
    pytest.main()
