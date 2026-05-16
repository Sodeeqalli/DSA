# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val

        def dfs(root):
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)

            leftVal = max(left, 0)
            rightVal = max(right, 0)

            nonlocal res
            res = max(root.val+ leftVal +rightVal, res)

            return root.val + max(leftVal, rightVal)

        dfs(root)
        return res
        