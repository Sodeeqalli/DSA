"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quadTree(n,r,c):
            sameVal = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        sameVal = False
                        break
            if sameVal:
                return Node(grid[r][c], True)
            else:
                n = n//2
                topLeft = quadTree(n, r, c)
                topRight = quadTree(n, r, c+n)
                bottomLeft = quadTree(n, r+n, c)
                bottomRight = quadTree(n, r+n, c+n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        return quadTree(len(grid), 0, 0)




        