# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse second half
        second_head = ListNode(0)
        while second:
            temp = second.next
            second.next = second_head.next
            second_head.next = second
            second = temp
        
        second_head = second_head.next
        final_dummy = ListNode(0)
        ptr = final_dummy

        while head and second_head:
            ptr.next = head
            ptr = ptr.next
            head = head.next
            ptr.next = second_head
            ptr = ptr.next
            second_head = second_head.next
        ptr.next = head
        head = final_dummy.next
