# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
- Fairly easy problem
- Trace the path followed by both elements from the root using BFS and maintain each path node's level
'''

class Solution:
    def find_path(self, root, node):
        from collections import deque
        queue = deque()
        queue.append(root)
        path = {}
        level = 1
        while queue:
            cur = queue.popleft()
            path[cur] = level 
            if cur.val == node.val:
                return path
            if cur.val > node.val:
                if cur.left:
                    queue.append(cur.left)
            elif cur.right:
                queue.append(cur.right)
            level += 1
        
        return path
                    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)

        lca = None
        lca_level = 0

        for elem in p_path:
            if elem in q_path:
                if p_path[elem] > lca_level:
                    lca = elem
                    lca_level = p_path[elem]

        return lca