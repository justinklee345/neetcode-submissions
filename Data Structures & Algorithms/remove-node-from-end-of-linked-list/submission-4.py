# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        
        idx = cnt - n
        print(idx)
        cnt = 0
        curr = head
        dummy = ptr = ListNode(-1)

        while curr:
            if idx != cnt:
                ptr.next = curr
                ptr = ptr.next
            cnt += 1
            curr = curr.next
        ptr.next = None

        return dummy.next
            

