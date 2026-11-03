class Solution:
    def rob(self, nums: list[int]) -> int:
        #at each decision point, you can either rob or skip
        #rob will take the value at that point then continue at cur + 2
        #or we can skip and continue at cur + 1

        n = len(nums)
        twoAhead = nums[-1]

        if n == 1:
            return twoAhead
        
        oneAhead = max(nums[-2], twoAhead)


        for i in range(n-3, -1, -1):
            rob = nums[i] + twoAhead
            skip = oneAhead
            curState = max(rob,skip)

            twoAhead = oneAhead
            oneAhead = curState

        return oneAhead
        