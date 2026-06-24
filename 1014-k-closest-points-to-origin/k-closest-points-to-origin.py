import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x,y in points:
            distance = (x**2) + (y**2)
            heap.append([distance, x, y])
        
        heapq.heapify(heap)

        while k > 0:
            _, resx, resy =  heapq.heappop(heap)
            res.append([resx, resy])
            k-=1
        
        return res

            
        
    
        
        
        
        


        