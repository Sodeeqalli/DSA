class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #num, space
        stack = [] #num, space
        maxArea = 0
        #[3,1]
        #[2,3]
        #[1,2]

        for height in heights:  
            space, prev = 1, 0
            while stack and stack[-1][0] > height:
                Rval, Rspace = stack.pop()
                areaofRemoved = Rval * (Rspace+prev)
                maxArea = max(maxArea, areaofRemoved)
                space += Rspace
                prev += Rspace
            stack.append([height,space])
        
        prev = 0
        while stack:
            Rval, Rspace = stack.pop()
            areaofRemoved = Rval * (Rspace+prev)
            maxArea = max(maxArea, areaofRemoved)
            prev += Rspace
        
        return maxArea




            
            





                

        