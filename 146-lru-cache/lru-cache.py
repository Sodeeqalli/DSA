class ListNode:
    def __init__(self, key = -1, value = -1, prev= None, nxt= None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.space = self.capacity = capacity
        self.nodeMap = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.space += 1
    
    def insert(self,node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        self.space -= 1

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return
        new = ListNode(key,value)
        self.nodeMap[key] = new
        self.insert(new)
        if self.space < 0:
            node = self.left.next
            del self.nodeMap[node.key]
            self.remove(node)
        return
            

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)