# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return
            invert(node.left)
            invert(node.right)
            ltemp = node.left
            rtemp = node.right
            node.right = ltemp
            node.left = rtemp
        invert(root)
        return root