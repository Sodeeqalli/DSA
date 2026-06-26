import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #smaller
        self.minHeap = [] #larger
        

    def addNum(self, num: int) -> None:
        #by default, we add to the smaller heap
        heapq.heappush(self.maxHeap, -num)
        #we make sure every number on maxHeap is smaller than minHeap
        while self.minHeap and self.maxHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        #then we balance the number
        while len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        while len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

            
    def findMedian(self) -> float:
        Slength, Blength = len(self.maxHeap), len(self.minHeap)
        if Slength == Blength:
            med = (-self.maxHeap[0] + self.minHeap[0])/2
        elif Slength > Blength:
            med = -self.maxHeap[0]
        else:
            med = self.minHeap[0]
        
        return med
        





        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()