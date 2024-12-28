# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Create dummy node for new linked list since the head pointer will be lost as you iterate through it
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        cur = new
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        
        return res.next