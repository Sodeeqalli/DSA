from collections import deque, Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        #take the count
        #2a 2b
        #then we use a queue to schedule the next place it can be avaialable, then we remove from the queue

        characterCount = Counter(s)

        maxHeap = [(-count,character) for character, count in characterCount.items()]
        heapq.heapify(maxHeap)
        q = deque()
        position = 0
        string = ""

        while maxHeap or q:
            
            position+=1

            if q and q[0][0] == position:
                _,countLeft, character = q.popleft()
                heapq.heappush(maxHeap, (countLeft, character))

            if maxHeap:
                count,character = heapq.heappop(maxHeap)
                string += character
                countLeft = count + 1
                nextPos = position + 2
                if countLeft < 0:
                    q.append([nextPos,countLeft,character])
            else:
                return ""
            
           
            
        return string

                

        