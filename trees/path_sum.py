# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Use DFS iteratively - for each node, add the total sum of the path it has traced until then
- If it is a leaf node and sum equals the target sum return true
- Can also use recursive - cleaner code but not as intuitive
'''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stck = [(root, root.val)]
        while stck:
            node, path_sum = stck.pop()
            
            if not node.left and not node.right and path_sum == targetSum:
                return True

            if node.right:
                stck.append((node.right, path_sum + node.right.val))
            if node.left:
                stck.append((node.left, path_sum + node.left.val))
        
        return False