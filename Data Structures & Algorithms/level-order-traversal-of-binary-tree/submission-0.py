# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        queue = deque([root])
        while len(queue) > 0:
            level_size = len(queue)
            current = []
            for _ in range(level_size):
                node = queue.popleft()
                if not node:
                    break
                current.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(current) > 0:
                traversal.append(current)
        return traversal
