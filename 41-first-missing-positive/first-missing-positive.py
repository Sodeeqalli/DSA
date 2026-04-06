class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #algorithm
        #anything less than 1 or greater than len of nums should be moved out of bounds
        #we go through array and mark the index of everything that is not out of bounds
        #we then start from the front of the array and return the very first non negative number

        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        for num in nums:
            if abs(num) != len(nums)+1:
                nums[abs(num)-1] = -1 * abs(nums[abs(num)-1])
        
        for index, num in enumerate(nums):
            if num > 0:
                return index + 1

        return len(nums) + 1


        




        