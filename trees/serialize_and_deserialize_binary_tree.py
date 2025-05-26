# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
- Individually, serialize and deserialize are easy problems. But need to ensure that the same approach (DFS/BFS) is used for both.
- Otherwise, the deseriliazation will work in a different order than the serialization.
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ["null"]
            
            res = [str(node.val)]
            res += dfs(node.left)
            res += dfs(node.right)

            return res
        
        return ",".join(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        self.index = 0
    
        def dfs():
            if data_list[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(data_list[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))