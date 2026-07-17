# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        left = self.howMany(root.left)
        right = self.howMany(root.right)

        if k == left + 1:
            return root.val
        elif k <= left:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - (left + 1))
        
        
    def howMany(self, root):
        if not root:
            return 0
        
        return 1 + self.howMany(root.left) + self.howMany(root.right)
        