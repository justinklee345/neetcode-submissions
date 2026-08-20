# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))
        
        dummy = ptr = ListNode(-1)
        while heap:
            popped = heapq.heappop(heap)

            ptr.next = popped.node
            ptr = ptr.next
            if not popped.node.next:
                continue
            heapq.heappush(heap, NodeWrapper(popped.node.next))
        
        return dummy.next



        