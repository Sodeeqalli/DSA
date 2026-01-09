class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minNum = float("inf")

        while l <= r:
            m = l + (r-l)//2
            minNum = min(minNum, nums[m])
            if nums[m] >= nums[l] and nums[l] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return min(minNum,nums[m])

                

        