# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        values = []

        def dfs(root):
            if not root:
                values.append("N")
                return
            
            values.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return (",").join(values)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        #[1,2,null, null,3,4, null, null, 5, null null]
        self.i = 0
        values = data.split(",")
        def constructTree():
            if values[self.i] == "N":
                self.i+=1
                return None 
            
            tree = TreeNode(str(values[self.i]))
            self.i+=1
            tree.left = constructTree()
            tree.right = constructTree()

            return tree
        
        return constructTree()


            
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))