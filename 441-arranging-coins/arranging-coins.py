class Solution:    
    def numOfCoins(self, Row):
        return (Row/2)*(Row+1)

    def arrangeCoins(self, n: int) -> int:
        l,r = 1, n
        res = 1

        while l <= r:
            m = l + (r-l)//2
            numCoins = self.numOfCoins(m)
            if numCoins > n:
                r = m - 1
            elif numCoins < n:
                res = m
                l = m + 1
            else:
                return m
        
        return res

                

            

        
        