# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        nodeVal = preorder[0]
        if len(preorder) == 1:
            return TreeNode(nodeVal)
        else:
            index = inorder.index(nodeVal)
            left = self.buildTree(preorder[1:index+1], inorder[:index])
            right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return TreeNode(nodeVal, left, right)

        
        

