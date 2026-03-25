class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)

        for s in strs:
            value = [0 for i in range(26)]
            for c in s:
                value[ord(c) - ord('a')] += 1 
            groupMap[tuple(value)].append(s)
        
        return list(groupMap.values())
            
         
            
        