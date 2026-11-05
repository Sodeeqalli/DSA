class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        #algorithm
        #i will take the sum of nums
        #check against modulo two if its not zero return false
        #get half by dividing into two
        #the state is the total so far and the index we at
        #at every index we take or skip
        #we return true if we ever reach half, False if we pass half

        sumOfNums = sum(nums)

        if sumOfNums % 2 != 0:
            return False
        
        half = sumOfNums // 2
    
        # memo = {}

        # def solve(sumLeft, index):
        #     if sumLeft < half:
        #         return False
        #     if sumLeft == half:
        #         return True
        #     if index == len(nums):
        #         return False
        #     if (sumLeft,index) in memo:
        #         return memo[(sumLeft, index)]
            
        #     #skip
        #     skip = solve(sumLeft, index+1)
        #     #take
        #     take = solve(sumLeft - nums[index], index + 1)

        #     memo[(sumLeft, index)] = skip or take

        #     return memo[(sumLeft, index)]
        

        # return solve(sumOfNums, 0)

        #bottom up
        #we are moving by index one at a time
        #we have to calculate the result of every index at every possibility of sumLeft
        #we know that if sumleft is less than half we return False
        #if sumleft == half, we return True
        #we know no matter what sumleft is, at index + 1, it is false
        #so we know how to calculate the very last state

        nextState = [False] * (sumOfNums+1)
        nextState[half] = True
        curState = [False] * (sumOfNums+1)

        for i in range(len(nums)-1, -1, -1):
            for j in range(half, sumOfNums+1):
                if j < half:
                    continue
                elif j == half:
                    curState[j] = True
                else:
                    skip = nextState[j]
                    take = False if j - nums[i] < half else nextState[j-nums[i]]
                    curState[j] = skip or take
            nextState = curState[:]
        

        return nextState[sumOfNums]
                

                







        