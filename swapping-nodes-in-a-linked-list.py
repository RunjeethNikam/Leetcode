from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        n1, n2 = None, None
        for _ in range(k):
            fast = fast.next
        n1 = fast
        slow = slow.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        n2 = slow
        n1.val, n2.val = n2.val, n1.val
        return dummy.next
    
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().swapNodes(ll, 2)