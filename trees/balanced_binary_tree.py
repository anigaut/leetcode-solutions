# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Very similar to Diameter of Binary Tree
- Solve it recursively - bottom-up
- Maintain a global variable to track if the tree is balanced or not
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs_height(node):
            if not node:
                return 0
            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            return 1 + max(left_height, right_height)
        
        dfs_height(root)
        return self.balanced
            
        return True   