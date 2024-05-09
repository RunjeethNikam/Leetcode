from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(node):
            if node:
                nxt = solve(node.next)
                if nxt and node.val < nxt.val:
                    node.next = None
                    return nxt
                else:
                    node.next = nxt
                    return node

        return solve(head)


node5 = ListNode(5)
node2 = ListNode(2)
node13 = ListNode(13)
node3 = ListNode(3)
node8 = ListNode(8)

# Link the nodes together
node5.next = node2
node2.next = node13
node13.next = node3
node3.next = node8


n = Solution().removeNodes(node5)
while n:
    print(n.val)
    n = n.next
