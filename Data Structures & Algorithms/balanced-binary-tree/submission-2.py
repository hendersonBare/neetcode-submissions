# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        diff = abs(self.calculateHeight(root.left) - self.calculateHeight(root.right))
        if (diff > 1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def calculateHeight(self, root) -> int:
        height = 1
        if root is None:
            return height
        else:
            return 1 + max(self.calculateHeight(root.left), 
                        self.calculateHeight(root.right))