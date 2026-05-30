# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = r = root
        lca = None
        while l and r:
            print(l.val, r.val)
            if l.val == r.val:
                lca = l
            if p.val == l.val or q.val == r.val:
                return lca
            if p.val < l.val:
                l = l.left
            elif p.val > l.val:
                l = l.right
            if q.val < r.val:
                r = r.left
            elif q.val > r.val:
                r = r.right
            print(l.val, r.val)
        return lca