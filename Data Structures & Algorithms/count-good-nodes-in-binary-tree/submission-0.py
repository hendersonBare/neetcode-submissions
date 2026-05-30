# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max):
            if node is None:
                return 0
            isGood = 0
            if node.val >= max:
                isGood = 1
                max = node.val
            return isGood + dfs(node.left, max) + dfs(node.right, max)
        return dfs(root, root.val)