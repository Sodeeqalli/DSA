class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        i = 0

        while i < len(nums)-3:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j < len(nums)-2:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                k,l = j+1, len(nums)-1

                while k<l:
                    sumVal = nums[i] + nums[j] + nums[k] + nums[l]
                    if sumVal > target:
                        l-=1
                    elif sumVal < target:
                        k+=1
                    else:
                        quads.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        while k < len(nums) and nums[k] == nums[k-1]:
                            k+=1
                
                j+=1
            i+=1
        
        return quads


        