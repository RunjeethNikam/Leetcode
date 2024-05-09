from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        sm = 0
        d = {0: dummy}

        curr = head
        while curr:
            sm += curr.val
            if sm in d:
                c = d[sm].next
                s = sm + c.val
                while s != sm:
                    del d[s]
                    c = c.next
                d[sm].next = curr.next
            else:
                d[sm] = curr
            curr = curr.next
        return dummy.next

ll = ListNode(1, ListNode(5, ListNode(5, ListNode(-5, ListNode(1)))))
ll = Solution().removeZeroSumSublists(ll)
while ll:
    print(ll.val)
    ll = ll.next

