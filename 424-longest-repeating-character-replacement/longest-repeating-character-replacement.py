class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characterCount = defaultdict(int)
        l = 0
        res = 0

        for r, c in enumerate(s):
            characterCount[c] += 1
            while l < len(s) and r - l + 1 - max(characterCount.values()) > k:
                characterCount[s[l]] -= 1
                l += 1 
            res = max(res, r-l+1)

        return res
            
            



        