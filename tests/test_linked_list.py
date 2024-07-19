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

    def test_insert(self, linked_list_without_head, linked_list_with_head):
        llnh = linked_list_without_head
        llnh.insert(2)
        llnh.insert(1)
        assert llnh.head.data == 1

        llh = linked_list_with_head
        assert llh.head.data == 1


    def test_search(self, linked_list_with_head, linked_list_without_head):
        llh = linked_list_with_head
        assert llh.search(1) == 0
        assert llh.search(2) == 1
        assert llh.search(3) == 2
        assert llh.search(4) == -1

        ll2 = linked_list_without_head
        assert ll2.search(3) == -1

    def test_delete(self, linked_list_without_head, linked_list_with_head):
        llnh = linked_list_without_head
        assert llnh.delete() is None

        llh = linked_list_with_head
        del_node = llh.delete()
        assert del_node.data == 1
        assert llh.head.data == 2
        assert llh.size() == 2

    # def test_display(self, capsys, linked_list_with_head, linked_list_without_head):
    #     linked_list_with_head.display()
    #     captured = capsys.readouterr()
    #     assert captured.out == "1 -> 2 -> 3 -> None\n"

    #     linked_list_without_head.display()
    #     captured = capsys.readouterr()
    #     assert captured.out == "Empty list\n"

if __name__ == "__main__":
    pytest.main()