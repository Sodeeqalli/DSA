class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        countArr = [[] for i in range(len(nums)+1)]

        for num,count in countMap.items():
            countArr[count].append(num)
        
        res = []
        for i in range(len(countArr)-1,-1,-1):
            if len(res) == k:
                return res
            while countArr[i]:
                res.append(countArr[i].pop())
        
        