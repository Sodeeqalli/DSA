import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #n piles of bananas
        #guards come back in h hours
        l = 1
        r = max(piles)
        minRate = 0
        
        while l <= r:
            m = l + ((r-l)//2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            
            if hours > h:
                l = m + 1
            else:
                minRate = m
                r = m - 1
        
        return minRate

