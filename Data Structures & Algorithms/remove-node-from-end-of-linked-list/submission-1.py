# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next

        to_delete = length - n
        cnt = 0
        while curr:
            if cnt == to_delete:
                prev.next = curr.next
                prev = curr
                curr = curr.next
                break
            cnt += 1
            prev = curr
            curr = curr.next
        
        return dummy.next

        