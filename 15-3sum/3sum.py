class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        [-1, -1,]
        nums.sort()
        i = 0
        triplets = []

        while i < len(nums)-2 and nums[i] < 1:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i + 1
            k = len(nums)-1

            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                if k < len(nums)-1 and nums[k] == nums[k+1]:
                    k-=1
                    continue
                sumVal = nums[i] + nums[j] + nums[k]
                if sumVal > 0:
                    k-=1
                elif sumVal < 0:
                    j+=1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    k-=1
            i+=1
        return triplets





        