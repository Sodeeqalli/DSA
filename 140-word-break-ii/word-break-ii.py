class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #understand yes
        #algorithm start from first letter and first end, if its a valid word, we continue throught that path, adding words to a list and when we are done with that path we remove the words from the list, then try another 


        #go

        currentWords = []
        res = []

        n = len(s)

        def backtrack(start):
            if start == n:
                res.append(" ".join(currentWords))
                return
            
            for end in range(start, n):
                if s[start:end+1] in wordDict:
                    currentWords.append(s[start:end+1])
                    backtrack(end+1)
                    currentWords.pop()
        
        backtrack(0)

        return res




        