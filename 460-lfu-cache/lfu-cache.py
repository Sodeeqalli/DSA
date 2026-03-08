#implementing list node building block
class ListNode:
    def __init__(self,value = -1,prev = None,nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt

#implementing doublylinked lists that would be used in LFU
class LinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self,val):
        node = ListNode(val,self.right.prev, self.right)
        self.right.prev.next = node
        self.right.prev = node
        self.map[val] = node
    
    def pop(self,val):
        if val in self.map:
            node = self.map[val]
            left,right= node.prev,node.next
            left.next = right
            right.prev = left
            self.map.pop(val, None)
    
    def popLeft(self):
        value = self.left.next.value
        self.pop(value)
        return value
    
    def update(self,val):
        self.pop(val)
        self.pushRight(val)

#implementing the cache itself

class LFUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {} #key -> value
        self.countMap = defaultdict(int) #key -> count
        self.listMap = defaultdict(LinkedList)
    
    def counter(self,key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)
        
        if cnt == self.lfuCount and self.listMap[cnt].length() == 0:
            self.lfuCount += 1
    
    def get(self,key):
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self,key, value):
        if self.cap == 0:
            return 
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popLeft()
            self.valMap.pop(res, None)
            self.countMap.pop(res, None)

        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.countMap[key], self.lfuCount)



    


