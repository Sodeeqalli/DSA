class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        #3,2,3,4
        #3-1
        #
        numCount = Counter(nums)
        countMap = defaultdict(int)
        for num in nums:
            countMap[num]+=1
            if countMap[num]>1 and len(countMap) > 1:
                tempMap = defaultdict(int)
                for count in countMap.values():
                    count -= 1
                for num, count in countMap.items():
                    if count > 0:
                        tempMap[num] = count
                countMap = tempMap

        res = []
        for num in countMap:
            if numCount[num] > len(nums)/3:
                res.append(num)
        
        return res

    #10,9,8,7,10,10,6,6
     #10,10
     #6
     #
     #   