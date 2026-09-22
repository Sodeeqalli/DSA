class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        n = len(nums)
        value = [0] * (max(nums)+3)

        for num in nums:
            value[num] += num

        dp = [0] * (max(nums)+3)
        m = len(dp)

        for i in range(m-3, -1, -1):
            dp[i] = max(value[i] + dp[i+2], dp[i+1])

        return dp[0]


        