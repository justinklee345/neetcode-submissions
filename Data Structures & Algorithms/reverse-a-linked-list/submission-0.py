# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        ptr = head
        while ptr != None:
            lst.append(ptr.val)
            ptr = ptr.next
        
        prev = None
        head = None
        for i in range(len(lst)-1, -1, -1):
            newNode = ListNode(lst[i], None)
            if i == len(lst) - 1:
                head = newNode
            if prev != None:
                prev.next = newNode
            prev = newNode

        return head

