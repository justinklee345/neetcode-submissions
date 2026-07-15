# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode(0, None)
        
        ptr = sum
        carry = False
        left = l1
        right = l2
        while left is not None or right is not None:
            added = 0
            if left and right:
                added = left.val + right.val
                left = left.next
                right = right.next   
            elif left:
                added = left.val
                left = left.next
            elif right:
                added = right.val
                right = right.next

            if carry:
                added += 1
                carry = False
            this_digit = added % 10
            if added >= 10:
                carry = True

            ptr.next = ListNode(this_digit, None)
            ptr = ptr.next
        
        if carry:
            ptr.next = ListNode(1, None)
            ptr = ptr.next

        return sum.next

