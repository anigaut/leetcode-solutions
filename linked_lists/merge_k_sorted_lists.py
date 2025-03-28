# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
- Fairly simple problem - from the back, merge each pair of lists and add the merged one back to the collection until there's only one element left in the input collection.
- Iteratively merge two lists
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            l1, l2 = lists[-1], lists[-2]

            merged = self.mergeTwoLists(l1, l2)
            lists.pop()
            lists.pop()
            lists.append(merged)
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        cur = res

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next

        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        
        return res.next