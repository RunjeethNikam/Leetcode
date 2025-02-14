from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # def merge(i, j, lists):
    #     dummy = ListNode(0)
    #     tail = dummy
    #     while lists[i] and lists[j]:
    #         if lists[i].val < lists[j].val:
    #             tail.next = lists[i]
    #             tail = tail.next
    #             lists[i] = lists[i].next
    #         else:
    #             tail.next = lists[j]
    #             tail = tail.next
    #             lists[j] = lists[j].next
    #     tail.next = lists[i] or lists[j]
    #     return dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     nodes = len(lists)
    #     interval = 1
    #     while interval < nodes:
    #         i = 0
    #         while i < nodes:
    #             lists[i] = self.merge(i, i + interval, lists)
    #             i += 2 * interval

    #         interval *= 2
    #     return lists[0] or None

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in lists:
            if i is not None:
                break
        else:
            return None
        head = tail = None
        count = len([i for i in lists if i])
        while count > 0:
            p = None
            mx = float("inf")
            index = 0
            while index < len(lists):
                h1 = lists[index]
                if h1 and h1.val < mx:
                    p = index
                    mx = h1.val
                index += 1
            if tail == None:
                head = tail = lists[p]
                lists[p] = lists[p].next
            else:
                tail.next = lists[p]
                tail = tail.next
                lists[p] = lists[p].next
            if lists[p] is None:
                count -= 1
        return head

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    #     def merge(a: ListNode, b: ListNode):
    #         dummy = ListNode(None)
    #         head = dummy
    #         while a and b:
    #             if a.val < b.val:
    #                 head.next = a
    #                 a = a.next
    #             else:
    #                 head.next = b
    #                 b = b.next
    #             head = head.next
    #         if a or b:
    #             head.next = a or b
    #         return dummy.next

    #     def merge_sort(i, j):
    #         if i > j:
    #             return []
    #         if i == j:
    #             return lists[i]

    #         left = merge_sort(i, (i + j) // 2)
    #         right = merge_sort(((i + j) // 2) + 1, j)
    #         combined = merge(left, right)
    #         return combined

    #     return merge_sort(0, len(lists) - 1)


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]
print(
    Solution().mergeKLists([])
)
