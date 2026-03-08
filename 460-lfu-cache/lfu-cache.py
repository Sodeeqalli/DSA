#implementing listNode
class ListNode:
    def __init__(self, value = -1, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt

#implementing Doubly Linked List
class LinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self):
        return len(self.map)
    
    def pushRight(self,value):
        node = ListNode(value, self.right.prev, self.right)
        node.prev.next = node
        self.right.prev = node
        self.map[value] = node
    
    def pop(self,value):
        if value in self.map:
            node = self.map[value]
            left = node.prev
            right = node.next
            left.next = right
            right.prev = left
            self.map.pop(value, None)
    
    def popLeft(self):
        if self.length() > 0:
            v = self.left.next.value
            self.pop(v)
            return v
        return None
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = {} #key to value
        self.lfuCount = 0
        self.freqMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)
    
    def counter(self, key):
        cnt = self.freqMap[key]
        self.freqMap[key] += 1

        if cnt > 0:
            self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)

        if self.lfuCount == cnt and self.listMap[self.lfuCount].length() == 0:
            self.lfuCount+=1
    
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.valMap:
            self.counter(key)
            self.valMap[key] = value
            return
        
        if len(self.valMap) == self.cap:
           evict = self.listMap[self.lfuCount].popLeft()
           self.valMap.pop(evict, None)
           self.freqMap.pop(evict, None) 
        
        self.valMap[key] = value
        self.freqMap[key] = 1
        self.listMap[1].pushRight(key)
        self.lfuCount = 1

        


