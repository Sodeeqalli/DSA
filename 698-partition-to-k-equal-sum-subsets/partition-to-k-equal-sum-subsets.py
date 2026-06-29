class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalNums = sum(nums)
        if not nums or totalNums % k != 0:
            return False
        
        target = totalNums // k
        if max(nums) > target:
            return False
        
        nums.sort(reverse = True)
        used = set()

        def backtrack(start, numBucket, curSum):
            if numBucket == k:
                return True
            
            seen = set()
            for i in range(start, len(nums)):
                if i in used:
                    continue
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                used.add(i)
                if nums[i] + curSum > target:
                    used.discard(i)
                    continue
                elif nums[i] + curSum == target:
                    if backtrack(0, numBucket+1, 0):
                        return True
                else:
                    if backtrack(i+1, numBucket, nums[i] + curSum):
                        return True
                used.discard(i)
            
            return False

        
        return backtrack(0, 0, 0)



            
        