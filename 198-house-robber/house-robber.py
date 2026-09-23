class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        dp2 = nums[-1]
        if n == 1:
            return dp2
        dp1 = max(nums[-2], nums[-1])
        if n == 2:
            return dp1
        
        for i in range(n-3, -1, -1):
            cur = max(nums[i]+dp2, dp1)

            dp2 = dp1
            dp1 = cur

        return cur


        







        