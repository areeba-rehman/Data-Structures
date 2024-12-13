class Node:
    def __init__(self, data, address = 0):
        self.data = data
        self.address = address


class XorLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        prev = 0
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        current_next = current.address ^ prev
        while current_next == None:
            current = current_next






        