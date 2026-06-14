import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            maxHeap.append(-num)
        
        heapq.heapify(maxHeap)

        i = 1

        while i < k:
            heapq.heappop(maxHeap)
            i+=1
        
        return -maxHeap[0]
        
        
        