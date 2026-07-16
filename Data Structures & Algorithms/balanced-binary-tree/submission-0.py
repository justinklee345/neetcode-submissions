# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return (True, 0)
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        this_height = max(left[1], right[1]) + 1

        if not left[0] or not right[0]:
            return (False, this_height)
        else:
            if abs(left[1] - right[1]) <= 1:
                return (True, this_height)
            else:
                return (False, this_height)