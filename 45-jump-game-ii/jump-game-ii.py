class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n

        dp[n-1] = 0


        for i in range(n-2, -1, -1):
            minimum = float("inf")

            
            for j in range(1,nums[i]+1):
                if i + j < n:
                    minimum = min(minimum, 1 + dp[i+j])
                   
            
            dp[i] = minimum


        return dp[0]


        