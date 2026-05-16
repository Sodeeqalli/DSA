class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search arrays
        m, n = len(matrix), len(matrix[0])
        l,r = 0, m-1
        index = float("-inf")

        while l<=r:
            mid = l + (r-l)//2

            if target > matrix[mid][n-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                index = mid
                break

        if index == float("-inf"):
            return False
        
        
        l,r = 0,n-1

        while l <= r:
            mid = l + (r-l)//2

            if target > matrix[index][mid]:
                l = mid + 1
            elif target < matrix[index][mid]:
                r = mid - 1
            else:
                return True
        
        return False








        #search array

        