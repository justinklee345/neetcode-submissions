# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root, subRoot, start):
            if start:
                if root and subRoot and root.val == subRoot.val:
                    return helper(root.left, subRoot.left, True) and helper(root.right, subRoot.right, True)
                elif not root and not subRoot:
                    return True
                return False
            
            if not root:
                return False

            if root.val != subRoot.val:
                return helper(root.left, subRoot, False) or helper(root.right, subRoot, False)
            else:
                return (helper(root.left, subRoot.left, True) and helper(root.right, subRoot.right, True)) or (helper(root.left, subRoot, False) or helper(root.right, subRoot, False))
        
        return helper(root, subRoot, False)
            
            