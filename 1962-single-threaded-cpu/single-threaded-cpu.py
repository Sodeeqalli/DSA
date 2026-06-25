import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskHeap = []
        for index, task in enumerate(tasks):
            taskHeap.append([task[0], task[1], index])
        heapq.heapify(taskHeap)
        availHeap = []
        res = []
        time = 0
    
        while taskHeap or availHeap:
            if not availHeap and time <= taskHeap[0][0]:
                time = taskHeap[0][0]
            
            while taskHeap and taskHeap[0][0] <= time:    
                _,processT, index = heapq.heappop(taskHeap)
                heapq.heappush(availHeap, [processT, index]) #1,2,4
                
            if availHeap:
                processT, index = heapq.heappop(availHeap) #
                time+= processT #0
                res.append(index) #1
            
            
        return res

                
            
                

            


                



        