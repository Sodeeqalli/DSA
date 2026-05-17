class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if len of s2 is less than s1 return False
        #we start at first 2 letters of s2, check if they contain same permutation
        if len(s2) < len(s1):
            return False

        s1Characters = [0] * 26
        s2Characters = [0] * 26

        for c in s1:
            value = ord(c) - ord("a")
            s1Characters[value] += 1
        
        for i in range(len(s1)):
            value = ord(s2[i]) - ord("a")
            s2Characters[value] += 1
        
        l = 0

        for r in range(len(s1), len(s2)):
            if s1Characters == s2Characters:
                return True
            
            leftVal = ord(s2[l]) - ord("a")
            s2Characters[leftVal] -= 1
            l+=1
            rightVal = ord(s2[r])-ord("a")
            s2Characters[rightVal] += 1
        
        return s1Characters == s2Characters

        



        