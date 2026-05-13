class Solution:    
    def arrangeCoins(self, n: int) -> int:
        stairCount = 0
        rowLength = 1
        while n >= rowLength:
            n-=rowLength
            stairCount += 1
            rowLength += 1
        return stairCount
        