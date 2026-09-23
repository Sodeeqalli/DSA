class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        #my top down approach
        n = len(s)

        memo = [None] * (n+1)

        setDict = set(wordDict)
        print(setDict)

        def solve(i):
            print(i)
            if i == n:
                return True
            if memo[i] != None:
                return memo[i]


            for end in range(i, n):
                if s[i:end+1] in setDict:
                    if solve(end+1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return solve(0)

        