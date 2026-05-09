# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            good = 0
            if node.val >= maxVal:
                good = 1
            maxVal = max(node.val, maxVal)
            return good + dfs(node.left, maxVal) + dfs(node.right,maxVal)
        return dfs(root,root.val)
        


        