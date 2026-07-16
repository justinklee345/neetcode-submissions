# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        traversed = []
        traversed_two = []
        queue = deque([p])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()

                if curr:
                    traversed.append(curr.val)
                else:
                    traversed.append(None)

                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
        
        queue = deque([q])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()

                if curr:
                    traversed_two.append(curr.val)
                else:
                    traversed_two.append(None)

                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
        
        
        return traversed == traversed_two
