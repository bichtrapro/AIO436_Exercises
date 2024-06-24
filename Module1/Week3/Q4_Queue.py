class MyQueue:
    def __init__(self, capacity) :
        self.__capacity = capacity
        self.__queue = []
    
    def is_empty(self):
        return len(self.__queue) == 0
    
    def is_full(self):
        return len(self.__queue) == self.__capacity
    
    def enqueue(self,value):
        if self.is_full():
            raise OverflowError("OVerflow")
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.__queue.pop(0)
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue[0]


myqueue = MyQueue(5)
myqueue.enqueue(1)
myqueue.enqueue(2)

print(myqueue.front())