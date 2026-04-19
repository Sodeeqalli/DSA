class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #[55, 30, 5, 4, 2]
        #[100, 20, 10, 10, 5]
        i = 0
        maxDistance = 0

        for index, num in enumerate(nums1):
            if index > i:
                i = index
            while i<len(nums2) and num <= nums2[i]:
                i+=1    
            maxDistance = max(maxDistance, i - index - 1)
            if i == len(nums2):
                break
        
        return maxDistance

            
            
                





        