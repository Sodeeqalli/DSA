class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        [100,4,200,1,3,2]

        setNums = set(nums)
        maxSeq = 0

        for num in nums:
            if num-1 in setNums or num not in setNums:
                continue
            val = num
            seq = 0
            while val in setNums:
                seq += 1
                setNums.remove(val)
                val += 1
            maxSeq = max(seq, maxSeq)
        
        return maxSeq

