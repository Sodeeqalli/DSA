import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskHeap = []
        for index, (enqueueT, processT) in enumerate(tasks):
            taskHeap.append([enqueueT, processT, index])
        heapq.heapify(taskHeap)
        availHeap = []
        time = 0
        res = []

        while taskHeap or availHeap:
            while taskHeap and time >= taskHeap[0][0]:
                _,processT, index = heapq.heappop(taskHeap)
                heapq.heappush(availHeap, [processT, index])
            
            if availHeap:
                processT, index = heapq.heappop(availHeap)
                time += processT
                res.append(index)
            else:
                time = taskHeap[0][0]
        
        return res


        
        
        
        