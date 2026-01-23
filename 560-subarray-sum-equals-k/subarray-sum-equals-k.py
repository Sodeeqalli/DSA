class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            if prefixSum - k in seen:
                count += seen[prefixSum - k]
            seen[prefixSum] += 1
        
        return count
            
            

