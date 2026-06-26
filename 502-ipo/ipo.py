class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #heap to prioritize by capital
        capHeap = []
        for p,c in zip(profits,capital):
            capHeap.append([c,-p])
        heapq.heapify(capHeap)
        
        #heap to prioritize by profit
        profitHeap = []

        #keep count of projects done so far
        numProjects = 0

        #keep count of capital
        cap = w

        while capHeap or profitHeap:
            while capHeap and capHeap[0][0] <= cap:
                _ ,profit = heapq.heappop(capHeap)
                heapq.heappush(profitHeap, profit)
            
            if not profitHeap:
                return cap
            
            if numProjects < k and profitHeap:
                cap -= heapq.heappop(profitHeap)
                numProjects += 1
            
            if numProjects == k:
                return cap
            
        return cap
            


        