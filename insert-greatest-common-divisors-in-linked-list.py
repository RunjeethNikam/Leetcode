from typing import Optional
from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head
        while curr:
            g = gcd(prev.val, curr.val)
            node = ListNode(g, curr)
            prev.next = node
            prev = curr
            curr = curr.next
            
        return head