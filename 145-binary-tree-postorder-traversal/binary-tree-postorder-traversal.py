# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [[root,False]],[]

        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    result.append(node.val)
                else:
                    stack.append([node, True])
                    stack.append([node.right, False])
                    stack.append([node.left, False])

        return result
        
        