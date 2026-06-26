class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #from is enqueue time
        #to is the dequeue time

        fromHeap = []
        toHeap = []

        for trip in trips:
            fromHeap.append([trip[1], trip[0]])
            toHeap.append([trip[2], trip[0]])

        heapq.heapify(fromHeap)
        heapq.heapify(toHeap)

        passangerCount = 0
     

        while fromHeap:
            position = fromHeap[0][0]

            while fromHeap and fromHeap[0][0] == position:
                _, passangers = heapq.heappop(fromHeap)
                passangerCount += passangers
            
            while toHeap and toHeap[0][0] <= position:
                _, passangers = heapq.heappop(toHeap)
                passangerCount -= passangers
            
            if passangerCount > capacity:
                return False
            
        return True

        



        