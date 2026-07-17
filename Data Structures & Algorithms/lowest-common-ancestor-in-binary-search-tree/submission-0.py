# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower, higher = 0, 0
        if p.val < q.val:
            lower = p.val
            higher = q.val
        else:
            lower = q.val
            higher = p.val

        curr = root
        while curr:
            if curr.val > higher:
                curr = curr.left
            elif curr.val < lower:
                curr = curr.right
            else:
                return curr
