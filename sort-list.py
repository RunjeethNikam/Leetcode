from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def divide(self, hd: ListNode):
        slow = hd
        fast = hd.next
        while fast and fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        return hd, h2             

    def sort(self, hd: ListNode):
        if hd:
            h1, h2 = self.divide(hd)
            if h1 and h2:
                h1 = self.sort(h1)
                h2 = self.sort(h2)
                head = tail = None
                while h1 or h2:
                    if getattr(h1, 'val', float('inf')) < getattr(h2, 'val', float('inf')):
                        if head == None:
                            head = tail = h1
                            h1 = h1.next
                        else:
                            tail.next = h1
                            tail = tail.next
                            h1 = h1.next
                    else:
                        if head == None:
                            head = tail = h2
                            h2 = h2.next
                        else:
                            tail.next = h2
                            tail = tail.next
                            h2 = h2.next
                return head
        return h1 or h2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head = self.sort(head)
        return head


h = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

Solution().sortList(h)