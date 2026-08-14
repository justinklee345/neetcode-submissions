# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def helper(root):
            nonlocal res
            
            if not root:
                return 0
            
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            res = max(res, left + right + root.val)
            return max(left, right) + root.val
        
        helper(root)
        return res