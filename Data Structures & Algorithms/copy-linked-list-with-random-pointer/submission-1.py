"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1)
        newPtr = newHead
        ptr = head
        mapping = {}
        while ptr:
            newNode = Node(ptr.val)
            newPtr.next = newNode
            newPtr = newPtr.next
            mapping[ptr] = newPtr
            ptr = ptr.next

        newPtr = newHead.next
        ptr = head

        while ptr:
            if ptr.random:
                newPtr.random = mapping[ptr.random]
            ptr = ptr.next
            newPtr = newPtr.next
        
        return newHead.next

        