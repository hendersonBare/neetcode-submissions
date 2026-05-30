# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def buildBst(node):
            if node is None:
                return []
            vals = buildBst(node.left)
            vals.append(node.val)
            vals.extend(buildBst(node.right))
            return vals
        bst = buildBst(root)
        return(bst[k-1])