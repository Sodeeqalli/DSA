from collections import deque
class MyStack:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        #[1,2,3,4]
        #[1,2,3]
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.popleft())
        x = self.stack1.popleft()
        self.stack2, self.stack1 = deque(), self.stack2
        return x


    def top(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()