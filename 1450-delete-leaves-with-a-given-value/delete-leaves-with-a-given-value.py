# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove(root, target):
            if not root:
                return [None,False]

            if not root.left and not root.right and target == root.val:
                return [None,True]
            
            dfsLeft = remove(root.left, target)
            dfsRight = remove(root.right, target)
        
            root.left = dfsLeft[0]
            root.right = dfsRight[0]

            return [root, dfsLeft[1] or dfsRight[1]]
        
        another = True
        resRoot = root
        while resRoot and another:
            resRoot, another = remove(root, target)

        return resRoot


        