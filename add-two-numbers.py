from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        result = l2
        carry = 0
        head = None
        tail = None
        while n1 or n2:
            sm = getattr(n1, 'val', 0) + getattr(n2, 'val', 0) + carry
            n1 = n1.next
            n2 = n2.next
            if sm > 9:
                carry = 1
                sm -= 10
            if tail == None:
                node = ListNode(sm)
                head = node
                tail = node
            else:
                tail.next = ListNode(sm)
                tail = tail.next
        return head