class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix) + 1, len(matrix[0])+1
        self.myMatrix = [[0]*col for i in range(row) ]
        for i in range(1,row):
            for j in range(1,col):
                self.myMatrix[i][j]= matrix[i-1][j-1] + self.myMatrix[i][j-1] + self.myMatrix[i-1][j] - self.myMatrix[i-1][j-1] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1 + 1,  col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.myMatrix[r2][c2]
        topRight = self.myMatrix[r1-1][c2]
        bottomLeft = self.myMatrix[r2][c1-1]
        intersection = self.myMatrix[r1-1][c1-1]
        return bottomRight + intersection - topRight - bottomLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)