class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if not current.left:
                current.left = new_node
                return
            
            else:
                queue.append(current.left)
                

            if not current.right:
                current.right = new_node
                return
            
            else:
                queue.append(current.right)
        
    def pre_order(self, node):
        if node:
            print(node.data, end= ",")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end = ",")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end = ",")

        
binary_tree = BinaryTree()
binary_tree.add('R')
binary_tree.add('A')
binary_tree.add('B')
binary_tree.add('C')
binary_tree.add('D')
binary_tree.add('E')
binary_tree.add('F')
binary_tree.add('G')

print("Preorder Traversal: ")
binary_tree.pre_order(binary_tree.root)

print("\nInorder Traversal: ") 
binary_tree.in_order(binary_tree.root)

print("\nPost Order Traversal: ")
binary_tree.post_order(binary_tree.root)

        

