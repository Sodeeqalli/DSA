class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        i = 0
        words = []

        while i < len(spaces):
            words.append(s[prev:spaces[i]])
            prev = spaces[i]
            i+=1
        
        words.append(s[prev:])

        return (" ").join(words)

            
        