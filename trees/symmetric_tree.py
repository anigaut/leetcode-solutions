# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Self-explanatory
- Don't get confused between identical and symmetrical trees
'''

class Solution:
    def same_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        return self.same_tree(root1.left, root2.left) and self.same_tree(root1.right, root2. right)

    def invert_tree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        
        self.invert_tree(root.left)
        return self.same_tree(root.left, root.right)