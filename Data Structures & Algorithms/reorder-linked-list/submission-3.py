# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        if not head.next:
            return

        fast, slow = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        mid = slow
        prev.next = None

        prev = None
        curr = mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l2 = prev
        l1 = head
        dummy = ptr = ListNode(0)

        while l1 and l2:
            ptr.next = l1
            ptr = ptr.next
            l1 = l1.next
            ptr.next = l2
            ptr = ptr.next
            l2 = l2.next
        
        if l2:
            ptr.next = l2

        head = dummy.next



