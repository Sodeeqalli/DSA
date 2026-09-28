class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
      
        n = len(questions)

        dp = [0]*(n)

        dp[n-1] = questions[n-1][0]
        dp[n-2] = max(dp[n-1],questions[n-2][0]) if n-2 + questions[n-2][1] + 1 >= n else max(questions[n-2][0] + dp[n-2 + questions[n-2][1]], dp[n-1])


        for state in range(n-3, -1, -1):
            next_state = None if state + questions[state][1] + 1 >= n else state + questions[state][1] + 1
            if next_state:
                answer_current = questions[state][0] + dp[next_state]
            else:
                answer_current = questions[state][0]
            
            skip_current = dp[state+1]

            dp[state] = max(answer_current, skip_current)

        
        return dp[0]



            




            
        