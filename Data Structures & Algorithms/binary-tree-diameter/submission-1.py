# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
        
    def helper(self, root: Optional[TreeNode]):
        if not root:
            return (0, 0)
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        return (max(left[0], right[0]) + 1, max(left[0] + right[0], left[1], right[1]))
