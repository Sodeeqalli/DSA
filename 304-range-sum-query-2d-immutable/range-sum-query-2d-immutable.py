class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_len, col_len = len(matrix)+1, len(matrix[0])+1
        self.myMatrix = [[0]*col_len for i in range(row_len)]
        for i in range(1,row_len):
            prefixSum = 0
            for j in range(1,col_len):
                prefixSum += matrix[i-1][j-1]
                self.myMatrix[i][j] = prefixSum + self.myMatrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomLeft = self.myMatrix[row2+1][col1] 
        topRight = self.myMatrix[row1][col2+1]
        bottomRight = self.myMatrix[row2+1][col2+1]
        topLeft = self.myMatrix[row1][col1]

        return bottomRight - topRight - bottomLeft + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)