class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        #my top down approach
#         n = len(s)

#         memo = [None] * (n+1)

#         setDict = set(wordDict)
#         print(setDict)

#         def solve(i):
#             print(i)
#             if i == n:
#                 return True
#             if memo[i] != None:
#                 return memo[i]


#             for end in range(i, n):
#                 if s[i:end+1] in setDict:
#                     if solve(end+1):
#                         memo[i] = True
#                         return True

#             memo[i] = False
#             return False

#         return solve(0)


#bottom up
        n = len(s)

        dp = [0] * (n+1)
        setDict = set(wordDict)

        dp[n] = True

        for i in range(n-1, -1, -1):
            canBreak = False
            for end in range(i,n):
                if s[i:end+1] in setDict:
                    if dp[end+1] == True:
                        canBreak = True
                        break
    
            dp[i] = canBreak

        return dp[0]
                
    

        
        