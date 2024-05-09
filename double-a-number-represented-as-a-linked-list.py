from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        head = reverse(head)
        carry = 0
        temp = head
        prev = None
        while temp:
            sm = temp.val * 2 + carry
            if sm > 9:
                carry = 1
                sm = sm % 10
            else:
                carry = 0
            temp.val = sm
            prev = temp
            temp = temp.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(head)
    

ll = ListNode(1, ListNode(8, ListNode(9)))
ll = Solution().doubleIt(ll)
while ll:
    print(ll.val)
    ll = ll.next