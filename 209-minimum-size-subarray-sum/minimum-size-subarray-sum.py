class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        minLen = float("inf")

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(r-l+1, minLen)
                currSum -= nums[l]
                l+=1

        return 0 if minLen == float("inf") else minLen

        