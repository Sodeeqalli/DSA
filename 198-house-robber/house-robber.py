class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        maxAmount = [0] * n
        maxAmount[n-1] = nums[n-1]
        maxAmount[n-2] = nums[n-2]
        maxAmount[n-3] = nums[n-3] + nums[n-1]

        for i in range(n-4, -1, -1):
            maxAmount[i] = nums[i] + max( maxAmount[i+2], maxAmount[i+3])

        return max(maxAmount[0], maxAmount[1])
        