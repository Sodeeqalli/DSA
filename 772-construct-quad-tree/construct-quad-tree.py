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
        def quadTree(heightStart, heightEnd, widthStart, widthEnd):
            sameVal = True

            for i in range(heightStart, heightEnd):
                for j in range(widthStart, widthEnd):
                    if grid[i][j] != grid[heightStart][widthStart]:
                        sameVal = False
                        break
                if not sameVal:
                    break

            if sameVal:
                return Node(grid[heightStart][widthStart] == 1, True)

            heightMid = (heightStart + heightEnd) // 2
            widthMid = (widthStart + widthEnd) // 2

            topLeft = quadTree(heightStart, heightMid, widthStart, widthMid)
            topRight = quadTree(heightStart, heightMid, widthMid, widthEnd)
            bottomLeft = quadTree(heightMid, heightEnd, widthStart, widthMid)
            bottomRight = quadTree(heightMid, heightEnd, widthMid, widthEnd)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return quadTree(0, n, 0, n)




        