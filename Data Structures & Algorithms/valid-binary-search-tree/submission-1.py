# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def buildBST(node):
            if node is None:
                return []
            vals = buildBST(node.left)
            vals.append(node.val)
            vals.extend(buildBST(node.right))
            return vals
        bst = buildBST(root)
        print(bst)
        prev = bst[0]
        for i in range(1, len(bst)):
            if bst[i] <= prev:
                return False
            prev = bst[i]
        return True
