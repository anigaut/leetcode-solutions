# Fast and slow pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                break
        return slow