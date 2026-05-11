class Solution:
    def trap(self, height: List[int]) -> int:
        
        #use a stack and go for every height 
        #if height is greater than or equal to the max, we add max - every number in the stack
        #when we get to the end and stack still remains, we remove the max, take new max and start from the right to calculate what each is worth
        if len(height) < 2:
            return 0
        stack = [] #[height]
        maxh = 0
        rainWater = 0

        for h in height:
            while stack and h >= maxh:
                removed = stack.pop()
                rainWater += maxh - removed
            stack.append(h)
            maxh = max(h, maxh)
        
        if stack:
            maxRight = 0
            for i in range(len(stack)-1 , 0 , -1):
                if stack[i] >= maxRight:
                    maxRight = stack[i]
                else:
                    rainWater += maxRight - stack[i]
            
        return rainWater







            


        
                


            

        