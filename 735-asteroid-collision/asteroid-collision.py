class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        #  -> positive
        # <- negative

        stack = []

        for a in asteroids:
            if a < 0:
                while a and stack and stack[-1] > 0:
                    if stack[-1]+a > 0:
                        a = 0
                    elif stack[-1]+a <0:
                        stack.pop()
                    else:
                        stack.pop()
                        a = 0
            if a:
                stack.append(a)
        
        return stack


                 


            
            
            

        