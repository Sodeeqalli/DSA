# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None

        mid = inorder.index(preorder[0])

        tree = TreeNode(preorder[0])
        left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        tree.left, tree.right = left, right
        return tree


            

            
            



        





        