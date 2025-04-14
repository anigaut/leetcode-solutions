# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Definitely not an easy problem
- Diameter is essentially the sum of the heights of the left and right subtrees
- But this need not always include the root, since the question asks for the longest path
- So, take the maximum diameter across all nodes in the tree - recursively
- Use DFS to find the height of the subtrees
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs_height(node):
            if not node:
                return 0
            
            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)

            self.res = max(self.res, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        dfs_height(root)
        return self.res