#linkedList
class ListNode:
    def __init__(self, value = -1):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = ListNode(-2)
        curr = self.q
        for i in range(k):
            curr.next = ListNode()
            curr = curr.next

        #-2 -> -1 -> -1 -> -1

        

    def enQueue(self, value: int) -> bool:
        #-2 -> -1 -> -1 -> -1
        curr = self.q
        while curr.next and curr.next.value != -1:
            curr = curr.next
        if curr.next:
            curr.next.value = value
            return True
        return False


        

    def deQueue(self) -> bool:
        #-2 -> 1 ->2->3
        curr = self.q
        if curr.next.value != -1:
            while curr.next:
                curr = curr.next
            curr.next = ListNode()
            curr = self.q
            curr.next = curr.next.next
            return True
        return False

        

    def Front(self) -> int:
        curr = self.q
        return curr.next.value
        
        

    def Rear(self) -> int:
        #-2 -> 1 ->2->3
        curr = self.q
        while curr.next and curr.next.value != -1:
            curr = curr.next
        return curr.value if curr != self.q else -1
        

    def isEmpty(self) -> bool:
        curr = self.q
        return True if curr.next.value == -1 else False
        

    def isFull(self) -> bool:
        #-2 -> 1 ->2->3
        curr = self.q
        while curr.next and curr.next.value != -1:
            curr = curr.next
        return False if curr.next else True

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()