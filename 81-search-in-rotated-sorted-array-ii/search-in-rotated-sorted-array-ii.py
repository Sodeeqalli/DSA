class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            
            if nums[m] == nums[l]:
                l += 1
            
            elif nums[m] > nums[l]:
                #left side
                if target > nums[m]:
                    l = m + 1
                else:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1

            else:
                if target < nums[m]:
                    r = m - 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        
        return False
        