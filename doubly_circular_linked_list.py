class Node:
    def __init__(self, data, prev= None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.prev = current
        new_node.next = self.head
        self.head.prev = new_node


    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        new_node.prev = self.head.prev

        current = self.head.prev
        
        current.next = new_node
        self.head.prev = new_node
        self.head = new_node


    def display(self, times=1):
        current = self.head
        count = 0

        while count < times:
            print(current.data, end=",")
            current = current.next

            if current == self.head:
                count += 1


                print()


Linked_List = DoublyCircularLinkedList()
Linked_List.append(3)
Linked_List.append(4)
Linked_List.append(5)
Linked_List.append(6)
Linked_List.prepend(2)
Linked_List.prepend(1)

Linked_List.display(3)