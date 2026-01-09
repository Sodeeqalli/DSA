class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(sumVal):
            split = 0
            curr = 0
            for num in nums:
                if curr + num > sumVal:
                    split += 1
                    curr = num
                else:
                    curr += num
            split += 1
            return True if split <= k else False

        l = max(nums)
        r = sum(nums)
        minimizedSum = r

        while l <= r:
            m = l + ((r-l)//2)
            if canSplit(m):
                minimizedSum = m
                r = m - 1
            else:
                l = m + 1
        
        return minimizedSum
            





        