class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #count, seq, letter

        countMap = {
            'a': a,
            'b': b,
            'c': c
        }

        maxHeap = [[-count,0,letter] for letter,count in countMap.items() if count > 0]
        heapq.heapify(maxHeap)
        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return res
            
            count, seq, letter = heapq.heappop(maxHeap)
            res+=letter
            count += 1
            seq += 1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            
            if count < 0:
                if seq < 2:
                    heapq.heappush(maxHeap,[count,seq,letter])
                else:
                    prev = [count, 0, letter]
        
        return res
        