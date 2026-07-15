# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)

        left = list1
        right = list2
        curr = dummy

        while left is not None or right is not None:
            if left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next

                else:
                    curr.next = right
                    right = right.next
            elif left:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        return dummy.next