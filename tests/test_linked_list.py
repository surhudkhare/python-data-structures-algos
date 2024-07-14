from multiprocessing import Value
from unittest.mock import patch
import pytest
from datastructures.linked_list import Node, LinkedList

class TestNode:
    def test_node_creation(self):
        node = Node(10)
        assert node.data == 10
        assert node.next is None

class TestLinkedList:
    """
    Tests for LinkedList operations
    """

    @pytest.fixture
    def linked_list_with_head(self):
        """Setup basic Linked List for testing"""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3
        return LinkedList(node1)
    
    @pytest.fixture
    def linked_list_without_head(self):
        return LinkedList()
    
    @pytest.fixture
    def list_input(self):
        return [1,2,3,4]

    def test_linked_list_creation(self, linked_list_without_head):
        ll_without_head = linked_list_without_head
        assert ll_without_head.head is None
        ll_with_head = LinkedList(Node(1))
        assert ll_with_head.head is not None
        assert ll_with_head.head.data == 1

    def test_search(self, linked_list_with_head, linked_list_without_head):
        linked_list = linked_list_with_head
        assert linked_list.search(1) == 0
        assert linked_list.search(2) == 1
        assert linked_list.search(3) == 2
        assert linked_list.search(4) == -1

        ll2 = linked_list_without_head
        assert ll2.search(3) == -1

    def test_display(self, capsys, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.display()
        captured = capsys.readouterr()
        assert captured.out == "1 -> 2 -> 3 -> None\n"

        linked_list_without_head.display()
        captured = capsys.readouterr()
        assert captured.out == "Empty list\n"

    def test_insert_head(self, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.insert(10, mode='head')
        assert linked_list_with_head.head.data == 10
        
        linked_list_without_head.insert(1, mode='head')
        assert linked_list_without_head.head.data == 1

    def test_insert_tail(self, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.insert(4, mode='tail')
        assert linked_list_with_head.head.next.next.next.data == 4

        linked_list_without_head.insert(1, mode='tail')
        assert linked_list_without_head.head.data == 1

    def test_insert_index(self, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.insert(5, mode='index', index=1)
        assert linked_list_with_head.head.next.data == 5

        linked_list_without_head.insert(1, mode='index', index=1)
        assert linked_list_without_head.head.data == 1

    def test_count_iterative(self, linked_list_with_head, linked_list_without_head):
        assert linked_list_with_head.count(mode='iterative') == 3
        assert linked_list_without_head.count(mode='iterative') == 0

    def test_count_recursive(self, linked_list_with_head, linked_list_without_head):
        assert linked_list_with_head.count(mode='recursive') == 3
        assert linked_list_without_head.count(mode='recursive') == 0

    def test_delete_value(self, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.delete(mode='value', value=2)
        assert linked_list_with_head.search(2) == -1

        with pytest.raises(IndexError):
            linked_list_without_head.delete(mode='value', value=1)

    def test_delete_index(self, linked_list_with_head, linked_list_without_head):
        linked_list_with_head.delete(mode='index', index=1)
        assert linked_list_with_head.search(2) == -1
        with pytest.raises(IndexError):
            linked_list_with_head.delete(mode='index', index = 3)
        with pytest.raises(IndexError):
            linked_list_without_head.delete(mode='index', index=0)


    def test_create_from_list(self, list_input):
        ll = LinkedList()
        ll.create(mode='list', node_list=list_input)
        assert ll.head.data == 4
        assert ll.head.next.data == 3
        assert ll.head.next.next.data == 2
        assert ll.head.next.next.next.data == 1
        assert ll.head.next.next.next.next is None

    def test_create_from_cli(self):
        user_input = "3 4 5 "
        with patch('builtins.input', return_value=user_input):
            ll = LinkedList()
            ll.create(mode='cli')
        assert ll.head.data == '5'
        assert ll.head.next.data == '4'
        assert ll.head.next.next.data == '3'
        assert ll.head.next.next.next is None

    def test_create_mode(self):
        ll = LinkedList()
        with pytest.raises(ValueError):
            ll.create(mode='random')

if __name__ == "__main__":
    pytest.main()