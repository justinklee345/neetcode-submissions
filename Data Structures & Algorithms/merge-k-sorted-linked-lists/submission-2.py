# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []

        for lst in lists:
            heapq.heappush(heap, NodeWrapper(lst))
        
        dummy = ptr = ListNode(0)
        while heap:
            popped = heapq.heappop(heap).node
            ptr.next = popped
            ptr = ptr.next
            if popped.next:
                heapq.heappush(heap, NodeWrapper(popped.next))
        return dummy.next
        