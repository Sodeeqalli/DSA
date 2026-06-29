class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #we try every partitioning from the start to atleast how many left before end
        #if len of current path equal to 4 we should stop and that means we can form a square
        #for every possible partition, if len of curr path is greater than 2 we check if the length of the matchstick = len of the matchstick 2 indices before it
        #if it is we continue through that path else we stop

        n = len(matchsticks)
        sumSticks = sum(matchsticks)
        if not matchsticks or sumSticks % 4 != 0:
            return False

        target = sumSticks // 4
        if max(matchsticks) > (target):
            return False
        
        sides = [0, 0, 0, 0]

        def backtrack(index):
            if index == n:
                return True
            
            seen = set()
            for i in range(len(sides)):
                if sides[i] in seen:
                    continue
                seen.add(sides[i])
                if sides[i] + matchsticks[index]  <= target:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]

            return False

        return backtrack(0)


        
    




        