class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def subMap(map1,map2):
            for c in map1:
                if map2[c] < map1[c]:
                    return False
            return True
        if len(t) > len(s):
            return ""
        tMap = Counter(t)
        sMap = defaultdict(int)
        l = 0
        minLen = float("inf")
        minInd = []

        for r in range(len(s)):
            sMap[s[r]] += 1

            if subMap(tMap,sMap):
                while subMap(tMap, sMap) and l < len(s):
                    sMap[s[l]] -= 1
                    l+=1
                if r - l + 2 < minLen:
                    minLen = r-l+2
                    minInd = [l-1,r] #real indices
            
        return "" if minLen == float("inf") else s[minInd[0]:minInd[1]+1]


            


            
    