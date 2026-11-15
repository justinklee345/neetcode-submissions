# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = head

        while ptr:
            temp = ptr.next
            ptr.next = dummy.next
            dummy.next = ptr
            ptr = temp
        
        ptr, prev = dummy, None

        for i in range(n):
            prev = ptr
            ptr = ptr.next
        
        prev.next = ptr.next
        
        head = dummy.next
        ptr = head
        dummy = ListNode(0)

        while ptr:
            temp = ptr.next
            ptr.next = dummy.next
            dummy.next = ptr
            ptr = temp
        
        return dummy.next
        
        