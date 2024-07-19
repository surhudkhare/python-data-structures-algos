from datastructures.stack import StackList
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
        stack.pop()
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

if __name__ == "__main__":
    pytest.main()
