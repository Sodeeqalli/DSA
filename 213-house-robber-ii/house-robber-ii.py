class Solution:
    def rob(self, nums: list[int]) -> int:
        def robHouses(houses):
            m = len(houses)

            twoAhead = houses[m-1]
            oneAhead = max(houses[m-2], twoAhead)

            for state in range(m-3, -1, -1):
                take = houses[state] + twoAhead
                skip = oneAhead

                decision = max(take,skip)

                twoAhead = oneAhead
                oneAhead = decision

        
            return oneAhead

        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        return max(robHouses(nums[1:]), robHouses(nums[:n-1]))
        
        