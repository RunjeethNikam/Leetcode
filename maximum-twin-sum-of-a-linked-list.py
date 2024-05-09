# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        curr = head
        result = float('-inf')
        def solve(h: ListNode):
            nonlocal curr
            nonlocal result
            if h:
                solve(h.next)
                result = max(result, h.val + curr.val)
                curr = curr.next
        
        solve(head)
        return result
    

ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(Solution().pairSum(ll))