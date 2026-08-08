# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        ptr = dummy
        first = list1
        second = list2
        while first or second:
            if first and second:
                if first.val <= second.val:
                    ptr.next = first
                    first = first.next
                    ptr = ptr.next
                else:
                    ptr.next = second
                    second = second.next
                    ptr = ptr.next
                continue
            
            if first:
                ptr.next = first
                first = first.next
                ptr = ptr.next
                continue
            
            if second:
                ptr.next = second
                second = second.next
                ptr = ptr.next
                continue
        return dummy.next
            


            