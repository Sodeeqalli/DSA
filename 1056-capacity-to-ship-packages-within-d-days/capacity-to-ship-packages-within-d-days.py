class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        minCapacity = 0

        while l<=r:
            m = l + ((r-l)//2)
            dayCount = 1
            curr = 0
            for weight in weights:
                if curr + weight > m:
                    dayCount += 1
                    curr = weight
                else:
                    curr += weight
            
            if dayCount > days:
                l = m + 1
            else:
                minCapacity = m
                r = m - 1
        
        return minCapacity


        