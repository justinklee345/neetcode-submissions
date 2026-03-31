# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.left == None and root.right == None:
            return root
        
        if root.left != None and root.right != None:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root
        elif root.left != None:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        elif root.right != None:
            root.left = self.invertTree(root.right)
            root.right = None
            return root