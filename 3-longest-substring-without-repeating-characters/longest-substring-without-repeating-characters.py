class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        maxLength = 0

        l = 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l+=1
            characters.add(s[r])
            maxLength = max(len(characters), maxLength)
        
        return maxLength
            



        
        