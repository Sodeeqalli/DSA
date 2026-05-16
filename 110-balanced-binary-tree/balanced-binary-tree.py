# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #if there is no root, its balanced
        #if there is no root.left and no root.right, its balance
        #then we check the depth of left and right, if the difference is greater than one we return False else True
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        leftHeight, rightHeight = depth(root.left), depth(root.right)

        if abs(leftHeight-rightHeight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



        