"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        q = deque()
    
        q.append(node)
        while q:
            curr = q.popleft()

            if curr not in oldToNew:
                oldToNew[curr] = Node(curr.val)
            
            for n in curr.neighbors:
                if n not in oldToNew:
                    q.append(n)
                    oldToNew[n] = Node(n.val)
                
                oldToNew[curr].neighbors.append(oldToNew[n])

        return oldToNew[node]
