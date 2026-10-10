class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        #at every spot you can either add or minus
        #if we get to the the last index + 1 and the sum = target, then thats one way
        #so for the last number there is up to target possibilities
        #so our last dp state will be an array of size target + 1
        
        # n = len(nums)
        # nextRow,currentRow = [0] * (target+1), [0] * (target+1)

        # nextRow[target] = 1


        # for i in range(n-1, -1, -1):
        #     for j in range(target+1):
        #         #add
        #         add = 0 if j + nums[i] > target else nextRow[j+nums[i]]
        #         subtract = 0 if j - nums[i] < 0 else nextRow[j-nums[i]]

        #         currentRow[j] = add + subtract
            
        #     nextRow = currentRow
        
        # return nextRow[0]

        #dont know how to represent negative with dp table form, imma use top down

        n = len(nums)
        memo = defaultdict(lambda:None)

        def solve(i, curSum):
            if i == n:
                if curSum == target:
                    return 1
                else:
                    return 0
            if memo[(i,curSum)] != None:
                return memo[(i, curSum)]
            
            add = solve(i + 1, curSum + nums[i])
            subtract = solve(i+1, curSum - nums[i])

            memo[(i, curSum)] = add + subtract

            return memo[(i, curSum)]


        return solve(0,0)          




        