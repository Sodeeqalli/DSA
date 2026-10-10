class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        #array of integers cost and an integer target
        #cost of painiting i+1 is given by cost i, so we have the cost of using digits 1 to 9
        #total cost must be equal to target
        #basically our function should return a string
        #we can only take if the integer is not bigger than the target
        #and we can use zero as the terminating character for invalid paths

        #create array of digits

        memo = defaultdict()


        def solve(i,curTarget):
            if curTarget == 0:
                return ""
            if i > 9:
                return None
            if (i,curTarget) in memo:
                return memo[(i,curTarget)]


            take = skip = None

            if cost[i-1] <= curTarget:
                takePath = solve(i, curTarget-cost[i-1])
                if takePath is not None:
                    take =  takePath + str(i)

            skipPath = solve(i+1, curTarget)
            if skipPath is not None:
                skip = skipPath

            if take is None and skip is None:
                memo[(i,curTarget)] = None
                return memo[(i,curTarget)]
            if take is None:
                memo[(i,curTarget)] = skip
                return memo[(i,curTarget)]
            if skip is None:
                memo[(i,curTarget)] = take
                return memo[(i,curTarget)]
            
            takeLen, skipLen = len(take), len(skip)

            if takeLen > skipLen: 
                memo[(i,curTarget)] = take
                return memo[(i,curTarget)]
            if skipLen > takeLen: 
                memo[(i,curTarget)] = skip
                return memo[(i,curTarget)]

            if take > skip: 
                memo[(i,curTarget)] = take
                return memo[(i,curTarget)]

            
            if skip > take: 
                memo[(i,curTarget)] = skip
                return memo[(i,curTarget)]
            
        answer = solve(1,target)
        return "0" if not answer else answer



            
            

        
        