# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Reverse the second half of the list (need to find the middle for this) and then merge the two halves in an alternating sequence
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding the middle of the list - second half begins after slow
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the second half
        current = slow.next # Head of the second half
        prev = None
        slow.next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        first_half = head
        second_half = prev

        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2