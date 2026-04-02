# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #question understood
        #go to every node and then run same tree if the node is the same as the root of subroot
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            return sameTree(root1.left, root2.left) and sameTree(root1.right,root2.right)
        stack=[root]
        
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    if sameTree(node,subRoot):
                        return True
                stack.append(node.right)
                stack.append(node.left)
        
        return False
       
        

        