class QueueX:
    def __init__(self, max_size = 3):
        self.__list = []
        self.__max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            print("The list is full")
            return
            
        self.__list.append(item)

    def dequeue(self):
        if len(self.__list) == 0:
            print("empty list")
            return
        
        return self.__list.pop(0)
        


    def peek(self):
         if len(self.__list) == 0:
            print("empty list")
            return
         
         return self.__list[0]
    
    def is_empty(self):
        return len(self.__list) == 0
    
    def size(self):
        return len(self.__list)
    
    def is_full(self):
        return len(self.__list) == self.__max_size
    

    def display(self):
        for item in self.__list:
            print(item, end = ",")
            
        print()

queue = QueueX(3)
print("is empty", queue.is_empty())
print("the size of list is ", queue.size())
print("is full ", queue.is_full())
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.display()

print("is empty", queue.is_empty())
print("the size of list is ", queue.size())
print("is full ", queue.is_full())
print("first element", queue.peek())
print("element" , queue.dequeue())
print("first element", queue.peek())
queue.display()


