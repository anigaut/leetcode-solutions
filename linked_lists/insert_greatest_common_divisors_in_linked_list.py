# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(a, b):
            if a == b:
                return a
            elif a > b:
                a, b = b, a

            res = a

            while res > b // 2:
                res = res // 2

            while True:
                if a % res == 0 and b % res == 0:
                    return res
                res -= 1

        cur = head

        while cur.next:
            temp = cur.next
            gcd = get_gcd(cur.val, temp.val)
            new = ListNode(gcd, temp)
            cur.next = new
            cur = temp

        return head