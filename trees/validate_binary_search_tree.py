# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
- Interesting problem
- Remember that all values in the left subtree of a node must be less than the node's value and all values in the right subtree must be greater than the node's value
- For each node, the value can fall within a particular range based on its parent and ancestor nodes - this is the key.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, (-float("inf"), float("inf")))]

        while stack:
            cur, limits = stack.pop()
            if cur.val <= limits[0] or cur.val >= limits[1]:
                return False
            
            if cur.right:
                stack.append((cur.right, (cur.val, limits[1])))
            if cur.left:
                stack.append((cur.left, (limits[0], cur.val)))
        
        return True
