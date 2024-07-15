class Node:
    def __init__(self, data):
        """
        A Node of a Singly-linked Linked List
        """
        self.data = data
        self.next = None

class LinkedList():
    """A dynamic linear data structure of linked nodes where each node contains data and reference to the next node
    It can be accessed by the first element 'head'
    """
    def __init__(self, head=None):
        self.head = head
    
    def search(self, value):
        """Method to find an element in a Linked List and return the index of the element
        Args:
            value (int/str): Element to find
        Returns:
            int: -1 if element not found, index value if found (0-n)
        """
        if self.head is None:
            return -1
        
        current = self.head
        idx = 0
        while current:
            if current.data == value:
                print(f"Element {value} found at index {idx}")
                return idx
            current = current.next
            idx += 1
        print(f"Element {value} not found")
        return -1
        
    
    def display(self):
        self.__display(self.head)
    
    def __display(self, head):
        """Takes the head of a Linked List and displays the whole LinkedList
        3->5->8->9
        Args:
            head (object of class Node): head of a Linked List
        """
        if head is None:
            print("Empty list")
            return 
        current = head
        while current.next:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data, "-> None")
    
    def create(self, mode, **kwargs):
        if mode == 'list':
            self.__create_from_list(kwargs['node_list'])
        elif mode == 'cli':
            self.__create_from_cli()
        else:
            raise ValueError("Please enter a valid mode - 'list' or 'cli'")
        
    def __create_from_list(self, node_list):
        for node_value in node_list:
            self.insert(node_value, mode='head')

    def __create_from_cli(self):
        user_input = input("Enter the values of nodes separated by space: ")
        node_list = user_input.strip(" ").split(" ")
        for node_value in node_list:
            self.insert(node_value, mode='head')

    def insert(self, data, mode='head', **kwargs):
        if mode == 'head':
            self.head = self.__insert_helper(head=self.head, data=data, index=0)
        elif mode == 'tail':
            current_count = self.count(mode='iterative')
            self.head = self.__insert_helper(head=self.head, data=data, index=current_count)
        elif mode == 'index':
            self.head = self.__insert_helper(head=self.head, data=data, index=kwargs['index'])
        else:
            raise ValueError("Invalid mode - head/tail/index")
        return self.head

    def count(self, mode='iterative'):
        if mode == 'iterative':
            count = self.__iterative_count(head=self.head)
        elif mode == 'recursive':
            count = self.__recursive_count(head=self.head)
        else:
            raise ValueError("Enter a valid mode - iterative or recursive")
        return count
    
    def delete(self, mode='value', **kwargs):
        """Delete an element by value or by index and return the head of the resulting linked list
        Args:
            mode (int/str): 'value' or 'index'
        """
        if mode == 'value':
            deleted_node = self.__delete_by_value(value=kwargs['value'])
        elif mode == 'index':
            deleted_node = self.__delete_by_index(index=kwargs['index'])
        else:
            raise ValueError("Invalid mode - value/index")
        return deleted_node

    def __delete_by_value(self, value):
        if self.head is None:
            raise IndexError("No head, index out of range")
        current = self.head
        trailing_node = None
        while current:
            if current.data == value:
                # Adjust pointers
                trailing_node.next = current.next
                deleted_node = current
                current = None
                return deleted_node
            trailing_node = current
            current = current.next
        return None
    
    def __delete_by_index(self, index):
        if self.head is None:
            raise IndexError("No head, index out of range")

        current = self.head
        idx_current = 0
        trailing_node = None
        if index > self.count():
            raise IndexError("Index out of range")
        while idx_current < index and current:
            trailing_node = current
            current = current.next
            idx_current += 1
        trailing_node.next = current.next
        deleted_node = current
        return deleted_node

    def __iterative_count(self, head):
        if head is None:
            return 0
        count = 0
        current_node = head
        while current_node.next:
            count += 1
            current_node = current_node.next
        return count+1
    
    def __recursive_count(self, head):
        if head is None:
            return 0
        else:
            current = head
            return 1 + self.__recursive_count(current.next)

    def __insert_helper(self, head, data, index):
        """Inserts a new Node at the specified index (0-n) of 
        a Linked List that begins with the node 'head'
        0 = First node
        n = Last node
        Args:
            data (_type_): Can be any type
            index (int): Target index of the new Node
        """
        new_node = Node(data)
        
        # If its an empty list, ignore the index, put the new node as head
        if head is None:
            head = new_node
            return head

        # If list is empty is None and index = 0, insert at head
        if index == 0:
            new_node.next = head
            head = new_node
            return head

        # If list is empty is None and index is > 0, 
        # TODO - exception for index < 0
        current = head
        current_pointer = 0
        trailing_node = None
        while current_pointer < index:
            trailing_node = current
            current = current.next
            current_pointer += 1
        
        # Adjust pointers
        new_node.next = trailing_node.next
        trailing_node.next = new_node
        return head


if __name__ == "__main__":
    # l1 = LinkedList()
    # l1.display()
    # l1.insert(data=2)
    # l1.display()
    # l1.insert(data=4)
    # l1.insert(data=6)
    # l1.display()
    # l1.insert(mode='tail', data=3)
    # l1.display()
    # l1.insert(mode='index', data=9, index=2)
    # l1.display()
    # l1.search(2)
    # l1.search(99)
    # del_node = l1.delete(mode='value', value=9)
    # print(f"Delete node with data = {del_node.data}")
    # print(l1.count(mode='iterative'))

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    ll = LinkedList(node1)
    ll.search(3)

    l4 = LinkedList()
    l4.create(mode='list', node_list=[3,6,8])
    l4.display()

    l5 = LinkedList()
    l5.create(mode='cli')
    l5.display()