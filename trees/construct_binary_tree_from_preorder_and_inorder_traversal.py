# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- Not a straightforward problem
- Use recursion
- Note that the first element of preorder is always the root of the tree
- Using the index of the root in inorder, we can determine the left and right subtrees and which elements of the two input lists belong to which subtree
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root