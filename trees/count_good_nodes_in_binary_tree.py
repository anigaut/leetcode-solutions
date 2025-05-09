# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Use DFS to traverse the tree and also maintain the maximum node value in the path upto that node
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            cur, path_max = stack.pop()

            if cur.val >= path_max:
                good_nodes += 1
            
            if cur.right:
                stack.append((cur.right, max(cur.val, path_max)))
            if cur.left:
                stack.append((cur.left, max(cur.val, path_max)))
        
        return good_nodes