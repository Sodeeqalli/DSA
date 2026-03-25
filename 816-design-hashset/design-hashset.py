class ListNode:
    def __init__(self, key = -1, nxt = None):
        self.key = key
        self.next = nxt

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode() for i in range(10**4)]
        
    def hashKey(self,key):
        return key % 10**4
    
    def add(self, key: int) -> None:
        index = self.hashKey(key)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hashKey(key)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hashKey(key)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)