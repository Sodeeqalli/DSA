class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #[1,1,1]
        #[0,1,2,3]

        #[1,2,3]
        #[0,1,3,6]
        
        prefixSum = [0] * (len(nums)+1)
        sumMap = defaultdict(int)
        subArrayCount = 0

        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        for i in range(len(prefixSum)):
            complement = prefixSum[i] - k
            subArrayCount += sumMap[complement]
            sumMap[prefixSum[i]] += 1

        return subArrayCount


        
        