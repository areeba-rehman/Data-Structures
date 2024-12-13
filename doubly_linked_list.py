class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        current = self.head
        new_node.next = current
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=",")
            current = current.next


Linked_List = DoublyLinkedList()
Linked_List.append(3)
Linked_List.append(4)
Linked_List.append(5)
Linked_List.prepend(2)
Linked_List.prepend(1)

Linked_List.display()