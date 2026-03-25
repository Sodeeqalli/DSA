# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       1
#   2       3
#4     5  6     7
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [],[]
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            result.append(node.val)
            curr = node.right
        
        return result

            
            
        
        