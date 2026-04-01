class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in nums:
            if num+1 in numSet or num not in numSet:
                continue
            
            seq =  0
            while num in numSet:
                numSet.remove(num)
                seq += 1
                num-=1
            
            longestSeq = max(longestSeq, seq)
        
        return longestSeq
            

                

        

        