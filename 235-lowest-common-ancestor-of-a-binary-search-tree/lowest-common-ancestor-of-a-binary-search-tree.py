# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pAncestors = {}
        qAncestors = {}
        
        #search for p
        curr = root
        level = 1
        while curr:
            pAncestors[level] = curr
            if curr.val == p.val:
                curr = None
            elif curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right
            level+=1
        
        curr = root
        level = 1
        while curr:
            qAncestors[level] = curr
            if curr.val == q.val:
                curr = None
            elif curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
            level +=1

        while len(pAncestors) > len(qAncestors):
            pAncestors.pop(max(pAncestors.keys()), None)
        
        while len(qAncestors) > len(pAncestors):
            qAncestors.pop(max(qAncestors.keys()), None)
        
        while qAncestors[max(qAncestors.keys())] != pAncestors[max(pAncestors.keys())]:
            qAncestors.pop(max(qAncestors.keys()), None)
            pAncestors.pop(max(pAncestors.keys()), None)
        
        return qAncestors.pop(max(qAncestors.keys()), None)
        
        

        

            
            

        