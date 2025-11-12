"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from driver import *
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_map = {node.val : Node(node.val)}
        stack = [node]

        while stack:
            cur_node = stack.pop()
            clone = node_map[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in node_map:
                    node_map[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                clone.neighbors.append(node_map[neighbor.val])
        
        return node_map[node.val]