# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        head = None
        central_ptr = None

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                # both ptr1 and ptr2 left

                newNode = None
                if ptr1.val <= ptr2.val:
                    newNode = ListNode(ptr1.val, None)
                    ptr1 = ptr1.next
                else:
                    newNode = ListNode(ptr2.val, None)
                    ptr2 = ptr2.next

                if not head:
                    head = newNode
                    central_ptr = newNode
                else:
                    central_ptr.next = newNode
                    central_ptr = newNode
                
            elif ptr1:
                # only ptr1 still left
                newNode = ListNode(ptr1.val, None)
                if not head:
                    head = newNode
                    central_ptr = newNode
                else:
                    central_ptr.next = newNode
                    central_ptr = newNode
                ptr1 = ptr1.next
            else:
                # only ptr2 still left
                newNode = ListNode(ptr2.val, None)
                if not head:
                    head = newNode
                    central_ptr = newNode
                else:
                    central_ptr.next = newNode
                    central_ptr = newNode

                ptr2 = ptr2.next

        return head

