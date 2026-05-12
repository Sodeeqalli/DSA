# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        seenSet = set()
        parentMap = {root:[None,None]}
        
        while stack:
            node = stack.pop()
            if node:
                if node in seenSet:
                    if not node.left and not node.right and node.val == target:
                        if parentMap[node][0] == None:
                            return None
                        else:
                            if parentMap[node][1] == "l":
                                parentMap[node][0].left = None
                            else:
                                parentMap[node][0].right = None
                else:
                    stack.append(node)
                    seenSet.add(node)
                    parentMap[node.left] = [node, "l"]
                    parentMap[node.right] = [node, "r"]
                    stack.append(node.left)
                    stack.append(node.right)

        return root




                        

        
        


        