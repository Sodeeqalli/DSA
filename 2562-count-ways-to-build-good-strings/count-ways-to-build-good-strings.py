class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # memo = [None] * (high+1)

        # def solve(curLength):
        #     if curLength == high:
        #         return 0
            
        #     if memo[curLength] != None:
        #         return memo[curLength]
            
        #     zeroSpaceUsed = zero+curLength
        #     oneSpaceUsed = one+curLength
            
        #     zeroPath = onePath = 0
        #     if  zeroSpaceUsed <= high:
        #         if zeroSpaceUsed >= low:
        #             zeroPath = 1 + solve(curLength + zero)
        #         else:
        #             zeroPath = solve(curLength + zero)

        #     if  oneSpaceUsed <= high:
        #         if oneSpaceUsed >= low:
        #             onePath = 1 + solve(curLength + one)
        #         else:
        #             onePath = solve(curLength + one)

        #     memo[curLength] = zeroPath + onePath

        #     return memo[curLength]


        # return solve(0) % (10**9 + 7)

        dp = [0] * (high+1)
        dp[high] = 0

        for i in range(high-1, -1, -1):
            zeroSpaceUsed = zero+i
            oneSpaceUsed = one+i

            zeroPath = onePath = 0

            if zeroSpaceUsed <= high:
                if zeroSpaceUsed >= low:
                    zeroPath = 1 + dp[zeroSpaceUsed]
                else:
                    zeroPath = dp[zeroSpaceUsed]
            
            if oneSpaceUsed <= high:
                if oneSpaceUsed >= low:
                    onePath = 1 + dp[oneSpaceUsed]
                else:
                    onePath = dp[oneSpaceUsed]
                
            dp[i] = zeroPath + onePath

        return dp[0] % (10**9 + 7)



            

        