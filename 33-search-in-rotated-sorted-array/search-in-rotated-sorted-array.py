class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            
            #if we are in the left
            if nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m + 1
                else:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
            
            #if we are in the right
            else:
                if target < nums[m]:
                    r = m - 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1

        return -1



        