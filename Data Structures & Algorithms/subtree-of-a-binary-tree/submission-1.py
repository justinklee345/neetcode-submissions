# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot, False)

    def helper(self, root, subRoot, checking): 
        if checking:
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False    
            
            if root.val == subRoot.val:
                return self.helper(root.left, subRoot.left, True) and self.helper(root.right, subRoot.right, True)
            else:
                return False
        
        if not root and not subRoot:
            return False
        
        if not root or not subRoot:
            return False    
        
        first = False
        if root.val == subRoot.val:
            first = self.helper(root.left, subRoot.left, True) and self.helper(root.right, subRoot.right, True)

        return first or self.helper(root.left, subRoot, False) or self.helper(root.right, subRoot, False)

   