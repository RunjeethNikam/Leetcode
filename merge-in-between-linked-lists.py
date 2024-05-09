# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        dummy_1 = ListNode(-1, list1)
        prev = dummy_1
        curr = list1
        for index in range(b+1):
            if index == a:
                prev.next = list2
            prev = curr
            curr = curr.next

        while list2.next:
            list2 = list2.next
        list2.next = curr

        return dummy_1.next


ll1 = ListNode(
    10,
    ListNode(
        1,
        ListNode(
            13,
            ListNode(
                16,
                ListNode(
                    9,
                    ListNode(
                        5,
                    ),
                ),
            ),
        ),
    ),
)
ll2 = ListNode(100, ListNode(101, ListNode(102)))

Solution().mergeInBetween(ll1, 3, 4, ll2)
