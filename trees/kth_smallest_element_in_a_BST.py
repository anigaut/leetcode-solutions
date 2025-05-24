# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Use DFS to traverse the tree and collect the values in sorted order into a list.
- Better to do it this way than converting the tree into a list and then picking out the k-th smallest element based on the indices.
'''
class Solution:
    def bfs(self, root):
        if not root:
            return []
        return self.bfs(root.left) + [root.val] + self.bfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_nodes = self.bfs(root)
        return sorted_nodes[k - 1]