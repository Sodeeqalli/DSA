class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #[5,6,7,1,2,3,4]
        def reverse(arr, i, j):
            while i <= j:
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)

        return nums
        