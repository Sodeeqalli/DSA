from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            #queue
            queue = Deque([])
            #get counter of every task
            taskCount = Counter(tasks)
            #maxheap
            maxHeap = [-count for count in taskCount.values()]
            heapq.heapify(maxHeap)
            #time
            time = 1

            #[-1,-1] 
            #[]

            while maxHeap or queue:
                while queue and queue[0][1] == time:
                    task,_ = queue.popleft()
                    heapq.heappush(maxHeap,task)

                if maxHeap:
                    task = heapq.heappop(maxHeap)
                    task+=1
                    if task < 0:
                        queue.append([task, time + 1 + n])
                
                time+=1
            
            return time - 1




                












        