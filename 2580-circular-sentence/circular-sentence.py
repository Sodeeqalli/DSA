class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        print(words)

        n = len(words)

        for i in range(1,n):
            if words[i-1][-1] != words[i][0]:
                return False

        if words[-1][-1] != words[0][0]:
            return False

        
        return True



        