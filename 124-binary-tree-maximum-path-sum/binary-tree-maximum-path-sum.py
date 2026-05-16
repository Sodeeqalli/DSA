# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root):
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            leftVal, rightVal = max(left,0), max(right,0)

            nonlocal res
            res = max(res, root.val + leftVal +rightVal)
            return root.val + max(leftVal, rightVal)

        dfs(root)
        return res
        