# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Do BFS, whilst also maintaining the level of each node in the queue
- Need to return a list where each element is a list of all nodes in each level
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append((root, 0))
        level_nodes = {}
        while queue:
            node, level = queue.popleft()
            if level in level_nodes:
                level_nodes[level].append(node.val)
            else:
                level_nodes[level] = [node.val]
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            
        for level in level_nodes:
            res.append(level_nodes[level])
        
        return res