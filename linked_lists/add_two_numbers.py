# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
- Essentially, add the digits in reverse order, since the digits are reversed
- Remember to take the carry-over into account
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            digits_sum = val_l1 + val_l2 + carry

            new = ListNode(digits_sum % 10)
            carry = digits_sum // 10

            cur.next = new
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next