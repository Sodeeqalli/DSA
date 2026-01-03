class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col, row = len(matrix), len(matrix[0])

        #binary search to search value range
        l,r = 0, col - 1

        while l<=r:
            m = l+((r-l)//2) 
            lower,upper = matrix[m][0],matrix[m][row-1]
            if lower > target:
                r = m - 1
            elif upper < target:
                l = m + 1
            else:
                break
        
        if not (l<=r):
            return False
        
        #binary search to find value in array
        l,r =0, row-1

        while l<=r:
            mid = l + (r-l)//2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        