from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        t = None
        e = None
        count = 1
        while curr:
            if count >= left and count <= right:
                if count == left:
                    t = curr
                    e = prev

                    nxt = curr.next

                    prev.next = None
                    curr.next = prev
                    prev = curr
                    curr = nxt
                elif count == right:
                    nxt = curr.next
                    curr.next = prev
                    e.next = curr
                    t.next = nxt
                    curr = nxt
                    prev = t

                else:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
            else:
                prev = curr
                curr = curr.next
            count += 1 
        return dummy.next
    
    def print(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next
        


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, )))))
ll = Solution().reverseBetween(ll, 4, 5)
Solution().print(ll)