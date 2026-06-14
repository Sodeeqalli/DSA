import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #for every point, we calculate distance
        #then we heapify so we can have the minimum distance at the top
        #then we take k closest and add to a result list 

        res = []
        distance = []

        for index, point in enumerate(points):
            dist = (point[0]**2) + (point[1]**2)
            distance.append((dist,index))
        
        heapq.heapify(distance)

        for i in range(k):
            dist, ind = list(heapq.heappop(distance))
            res.append(points[ind])
        
        return res
            


        