# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        dummy = ListNode(0, None)
        ptr = dummy

        left = head
        right = prev
        while left is not None or right is not None:
            if left and right:
                ptr.next = left
                left = left.next
                ptr = ptr.next

                ptr.next = right
                right = right.next
                ptr = ptr.next
            elif left:
                ptr.next = left
                left = left.next
                ptr = ptr.next
            
            else:
                ptr.next = right
                right = right.next
                ptr = ptr.next
        
        head = dummy.next


        