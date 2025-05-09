# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Problem description is horrible
- Basically, find the rightmost node at every level
'''
class Solution:
    def level_nodes(self, root):
        from collections import deque
        ln = {}
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if level in ln:
                ln[level].append(node.val)
            else:
                ln[level] = [node.val]
        
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return ln
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightmost_nodes = []
        level_nodes = self.level_nodes(root)

        for level in level_nodes:
            rightmost_nodes.append(level_nodes[level][-1])
        
        return rightmost_nodes