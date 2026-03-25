#[]
#[3,2,1]


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

        

    def pop(self) -> int:
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        value = self.stack1.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return value

        

    def peek(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        value = self.stack2[-1]
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return value
        

    def empty(self) -> bool:
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()