class ListNode:
    def __init__(self,key = -1,value = -1,prev = None,nxt = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

     


    def __init__(self, capacity: int):
        self.space = capacity
        self.left = ListNode()
        self.right = ListNode(prev = self.left)
        self.left.nxt = self.right
        self.hashMap = {}
        # l-> <-r
        #2

    def get(self, key: int) -> int:
        if key in self.hashMap:
            v = self.hashMap[key].value
            self.put(key,v)
            return v
        return -1
        

        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            curr = self.hashMap[key]
            curr.prev.nxt = curr.nxt
            curr.nxt.prev = curr.prev
            self.space += 1
        new = ListNode(key,value,self.right.prev,self.right)
        self.right.prev.nxt = new
        self.right.prev = new
        self.space -= 1
        self.hashMap[key] = new
        if self.space == -1:
            del self.hashMap[self.left.nxt.key]
            self.left.nxt = self.left.nxt.nxt
            self.left.nxt.prev = self.left
            self.space+=1
        
        # l-> <-1-> <-3-> <-<-r
        # -1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)