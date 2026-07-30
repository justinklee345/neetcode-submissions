# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0 or len(preorder) <= 0:
            return None
        newNode = TreeNode(preorder[0])

        idx = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        newNode.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return newNode