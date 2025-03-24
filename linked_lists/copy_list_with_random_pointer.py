"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
'''
- A deep copy means that a new node must be created with the same properties as the old one for each element in the list - the copy is independent of the original.
- Two-pass solution: the first pass is to create a new nodes with the same values as the old ones. The second one is to assign the same "next" and "random" properties to the new one.
- Cannot assign references to the old nodes in the new ones.
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = { None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copy_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copy_map[cur]
            copy.next = copy_map[cur.next]
            copy.random = copy_map[cur.random]
            cur = cur.next
        
        return copy_map[head]