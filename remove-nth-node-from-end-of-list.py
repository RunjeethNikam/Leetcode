from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast = head
        while n:
            fast = fast.next
            n -= 1
        current = dummy
        while fast:
            current = current.next
            fast = fast.next
        current.next = current.next.next
        return dummy.next
        
