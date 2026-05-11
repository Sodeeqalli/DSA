class Solution:
    def trap(self, height: List[int]) -> int:
        
        #use a stack and go for every height 
        #if height is greater than or equal to the max, we add max - every number in the stack
        #when we get to the end and stack still remains, we remove the max, take new max and start from the right to calculate what each is worth

        maxLeft, maxRight = height[0] , height[-1]
        l,r = 0, len(height)-1
        rainWater = 0

        while l <= r:
            if maxRight < maxLeft:
                if maxRight > height[r]:
                    rainWater += maxRight - height[r]
                else:
                    maxRight = height[r]
                r-=1
            else:
                if maxLeft > height[l]:
                    rainWater += maxLeft - height[l]
                else:
                    maxLeft = height[l]
                l+=1
            
        return rainWater
                


        







            


        
                


            

        