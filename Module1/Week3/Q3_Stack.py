class MyStack:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__stack = []
    
    #Kiem tra stack empty
    def is_empty(self):
        return len(self.__stack)==0

    #Kiem tra stack full
    def is_full(self):
        return len(self.__stack)== self.__capacity
    #Them vao stack
    def push(self, value):
        if self.is_full():
            raise OverflowError("Overflow")
        self.__stack.append(value)
    #Xoa bo phan tu khoi stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__stack.pop()
    #lay phan tu tren cung
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.__stack[-1]
if __name__ == "__main__":
    mystack = MyStack(5)
    mystack.push(1)
    mystack.push(2)
    print(mystack.is_full())
    print(mystack.top())
    print(mystack.pop())
    print(mystack.top())
    print(mystack.pop())
    print(mystack.is_empty())