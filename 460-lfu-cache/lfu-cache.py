#implementing a listNode
class ListNode:
    def __init__(self,value = -1,prev = -1,nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt

#implementing a doubly linked list

class LinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.map = {}
        self.left.next = self.right
        self.right.prev = self.left

    def length(self):
        return len(self.map)
    
    def pushRight(self,value):
        node = ListNode(value,self.right.prev,self.right)
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
            value = self.left.next.value
            self.pop(value)
            return value
        return None

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity                         #capacity
        self.lfuCount = 0                           #the least frequent count
        self.valMap = {}                            #map of keys to values
        self.freqMap = defaultdict(int)             #frequency of keys
        self.ListMap = defaultdict(LinkedList)      #Linkedlist of each frequency
    
    def counter(self, key):
        #current freq of the key
        cFreq = self.freqMap[key]
        #increase by one
        self.freqMap[key] += 1
        if cFreq > 0:
            self.ListMap[cFreq].pop(key)
        self.ListMap[cFreq+1].pushRight(key)
        if cFreq == self.lfuCount and self.ListMap[self.lfuCount].length() == 0:
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
            self.valMap[key] = value
            self.counter(key)
            return

        if len(self.valMap) == self.cap:
            evict = self.ListMap[self.lfuCount].popLeft()
            self.valMap.pop(evict, None)
            self.freqMap.pop(evict,None)
        
        self.valMap[key] = value
        self.ListMap[1].pushRight(key)
        self.freqMap[key] = 1
        self.lfuCount = 1





# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)