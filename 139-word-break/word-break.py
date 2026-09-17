class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        #this very tricky to me
        #i am not quite sure what the state is, maybe we start from the actual first letter
        #i think i get it now, we can access future states so for current state we just check for every other index, when we see a word in the dictionary we start from the next letter
        n = len(s)
        setDict = set(wordDict)
        memo = [None] * n
        def breakWord(i):
            if i == n:
                return True
            if memo[i] != None:
                return memo[i]
            
            for end in range(i,n):
                if s[i:end+1] in wordDict:
                    if breakWord(end+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return breakWord(0)
