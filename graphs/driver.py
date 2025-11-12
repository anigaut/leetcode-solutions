
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:
    def __init__(self, node) -> None:
        self.nodes = [node]
    
    def display_adj_list(self):
        adj_list = []
        for node in self.nodes:
            adj_list.append(node.neighbors)