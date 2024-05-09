from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp
        return None
        
y = ListNode(4)
z = ListNode(2, ListNode(0, y))
y.next = z

x = ListNode(3, z)
Solution().detectCycle(x)
