from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, start, end):
        prev = None
        t = start
        while start != end:
            nxt = start.next
            start.next = prev
            prev = start
            start = nxt
        return prev, t


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        slow = prev.next
        fast = prev.next
        while True and fast:
            for i in range(k):
                fast = fast.next
                if not fast and i < (k-1):
                    return dummy.next
            else:
                h, t = self.reverse(slow, fast)
                prev.next = h
                prev = t
                slow = fast

ll = ListNode(1, ListNode(2))
print(Solution().reverseKGroup(ll, 2))
