# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #           1
        #      2          3
        #   4     5    6     7
        
        stack, visited = [root], [False]
        result = []

        while stack:
            node, v = stack.pop(), visited.pop()
            if node:
                if v:
                    result.append(node.val)
                else:
                    stack.append(node)
                    visited.append(True)
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)
            
        return result


