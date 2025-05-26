# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Quite similar to the diameter of binary tree problem.
- But remember that negative values in the trees can bring down the sum.
- So consider subtree sums only if they are positive.
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        def dfs_sum(node):
            if not node:
                return 0

            left_sum_positive = max(dfs_sum(node.left), 0)
            right_sum_positive = max(dfs_sum(node.right), 0)

            self.max_sum = max(self.max_sum, 
            node.val + left_sum_positive + right_sum_positive)

            return node.val + max(left_sum_positive, right_sum_positive)
        
        dfs_sum(root)
        return self.max_sum