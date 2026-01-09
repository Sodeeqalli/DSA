class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #[1,2]
        #[3,4]
        
        #ideally median should be middle

        #we find half of the length of both
        #we run a binary search on smaller list and get middle
        #then we do half-middle as where we stop in the other list
        #so we check if the last num in A is smaller than first num in second half of b vice versa.
        #if the last num in A is bigger, we move binary search backwards, else we move it forward
        #when it finally satisfies, we are one step closer to finding the median. if it is odd, we take the min of the side after, if its even, we take the max of the left side and min of right side
        A,B = nums1, nums2
        total = len(A) + len(B)
        half = total//2

        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0, len(A)-1

        while True:
            lma = l + ((r-l)//2)

            lmb = half - lma - 2

            leftFigureA = A[lma] if lma >= 0 else float("-infinity")
            rightFigureA = A[lma+1] if lma+1 < len(A) else float("infinity")
            leftFigureB = B[lmb] if lmb >=0 else float("-infinity")
            rightFigureB = B[lmb+1] if lmb+1 < len(B) else float("infinity")

            if leftFigureA > rightFigureB:
                r = lma - 1
            elif leftFigureB > rightFigureA:
                l = lma + 1
            else:
                if total % 2:
                    return min(rightFigureB,rightFigureA)
                else:
                    return (min(rightFigureB,rightFigureA) + max(leftFigureA,leftFigureB))/2








        