from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = h2 = None
        t1 = t2 = None
        count = 0
        curr = head
        while curr:
            nxt = curr.next
            curr.next = None
            if (count % 2) == 0:
                if h1 is None:
                    h1 = t1 = curr
                else:
                    t1.next = curr
                    t1 = t1.next
            else:
                if h2 is None:
                    h2 = t2 = curr
                else:
                    t2.next = curr
                    t2 = t2.next

            curr = nxt
            count += 1

        t1.next = h2
        return h1
