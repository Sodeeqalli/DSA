class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        nums.sort()
        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return

            
            #include
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #exclude
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)
        
        backtrack(0)

        return res
            
        