class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def display(self):
        current = self.head
        display_string = "Empty List"
        while current:
            if current == self.head:
                display_string = str(current.data)
            else:
                display_string = display_string + "->" + str(current.data)
            current = current.next
        print(display_string)
 
    def __str__(self) -> str:
        current = self.head
        display_string = "Empty List"
        while current:
            if current == self.head:
                display_string = str(current.data)
            else:
                display_string = display_string + "->" + str(current.data)
            current = current.next
        return display_string

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        return

    def delete(self):
        if self.head is None:
            return
        deleted_node = self.head
        self.head = deleted_node.next
        return deleted_node

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.display()
    llist.delete()
    llist.display()
    print(llist)