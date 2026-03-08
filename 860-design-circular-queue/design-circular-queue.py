class ListNode:
    def __init__(self,value = -1,prev = -1,nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = self.capacity = k
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            node = ListNode(value)
            node.prev =  self.right.prev
            node.prev.next = node
            node.next = self.right
            self.right.prev = node
            self.space -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.space += 1
            return True
        return False
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.next.value
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.prev.value
        return -1
        

    def isEmpty(self) -> bool:
        return self.space == self.capacity
        

    def isFull(self) -> bool:
        return self.space == 0
        
#left -> 2 3 4<- right

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()