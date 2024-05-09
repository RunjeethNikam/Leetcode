from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def reverse(self, ll):
        prev = None
        curr = ll
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        ll1 = head
        ll2 = slow.next
        slow.next = None

        ll2 = self.reverse(ll2)

        while ll1 and ll2:
            if ll1.val != ll2.val:
                return False
            else:
                pass
            ll1 = ll1.next
            ll2 = ll2.next
        return True
    


ll = ListNode(1, ListNode(0, ListNode(0)))
print(Solution().isPalindrome(ll))