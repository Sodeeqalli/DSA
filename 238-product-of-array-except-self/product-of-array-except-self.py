class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        #[1,2,3,4]
        #[1,1,2,6]
        #[1,12,8,6]
        product = [1 for i in range(len(nums))]
        
        pre = 1
        for i in range(1, len(nums)):
            pre*=nums[i-1]
            product[i]*=pre
            

        post = 1
        for i in range(len(nums)-2, -1, -1):
            post *= nums[i+1]
            product[i] *= post
            

        return product



        