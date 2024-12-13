class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            print("empty list")
            return
        
        last_element = self.list.pop()
        return last_element
    

    def peek(self):
        if len(self.list) == 0:
            print("empty list")
            return
        
        return self.list[-1]
        
        


stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)
print("last element", stack.peek())
print("element", stack.pop())
print("element", stack.pop())
print("element", stack.pop())  

print(stack.list)
stack.list.append(5)
print(stack.list)