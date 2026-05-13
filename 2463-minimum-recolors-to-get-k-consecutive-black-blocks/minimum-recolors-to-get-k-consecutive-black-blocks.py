class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        

        for i in range(k):
            if blocks[i] == 'W':
                white += 1
            
        minWhite = white
        
        l = 0
        for r in range(k, len(blocks)):
            if blocks[r] == 'W':
                white += 1
            if blocks[l] == 'W':
                white -= 1
            l+=1
            minWhite = min(minWhite, white)
        
        return minWhite
            
            
            



        