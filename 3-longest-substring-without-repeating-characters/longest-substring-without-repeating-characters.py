class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = defaultdict(int)
        maxLength = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while max(count.values()) > 1:
                count[s[l]] -= 1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength



        