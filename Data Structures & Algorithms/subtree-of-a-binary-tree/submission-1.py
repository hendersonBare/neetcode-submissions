# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if ((p is None and q is not None) or (p is not None and q is None)):
                return False
            if p is None and q is None:
                return True
            return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right, q.right)
        
        def dfs(node, target):
            if node is None:
                return isSameTree(node, target)
            return isSameTree(node, subRoot) or dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, subRoot)
        