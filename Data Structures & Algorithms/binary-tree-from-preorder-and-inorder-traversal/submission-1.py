# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print(preorder, inorder)
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None
        newNode = TreeNode(preorder[0])

        split = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1:split+1], inorder[:split])
        newNode.right = self.buildTree(preorder[split + 1:], inorder[split + 1:])
        return newNode