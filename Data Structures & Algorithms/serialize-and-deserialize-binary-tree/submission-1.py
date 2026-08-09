# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import ast

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        queue = deque()
        queue.append(root)
        while queue:
            val = queue.popleft()
            if not val:
                res.append("null")
                continue
            
            res.append(val.val)
            queue.append(val.left)
            queue.append(val.right)

        return str(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = ast.literal_eval(data)
        if data[0] == "null":
            return None
        
        root = TreeNode(int(data[0]))
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if data[idx] != "null":
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            idx += 1
            if data[idx] != "null":
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            idx += 1
        return root





        return None