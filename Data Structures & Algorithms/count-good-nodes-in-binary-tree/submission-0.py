# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float('-inf'))
    
    def helper(self, root, curr_max):
        if not root:
            return 0
        
        if root.val >= curr_max:
            return 1 + self.helper(root.left, max(curr_max, root.val)) + self.helper(root.right, max(curr_max, root.val))
        else:
            return self.helper(root.left, curr_max) + self.helper(root.right, curr_max)