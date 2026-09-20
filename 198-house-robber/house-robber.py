class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2], nums[n-1])

        for i in range(n-3, -1, -1):
            skip = dp[i+1]
            rob = nums[i] + dp[i+2]

            dp[i] = max(rob, skip)
        
        return dp[0]
        