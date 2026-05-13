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
        maxVal = root.val

        def maxSum(root):
            if not root:
                return [0,0]
            
            left, right = maxSum(root.left), maxSum(root.right)
            forSelf = max (left[1] + right[1] + root.val, max(left[1], right[1]) + root.val, root.val)
            forParent = max(max(left[1], right[1]) + root.val, root.val)
            nonlocal maxVal
            
            maxVal = max(maxVal, forSelf)
    
            return [forSelf, forParent]
        
        maxSum(root)

        return maxVal
            




