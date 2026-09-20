class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        #how many ways can we decode last digit
        if s[n-1] == "0":
            dp[n-1] = 0
        else:
            dp[n-1] = dp[n]

        if n == 1:
            return dp[0]
        
        #how many ways can we second to last digit

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7):
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]

        
        return dp[0]




        
        

    

            









            


        