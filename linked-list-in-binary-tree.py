from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(r, h):
            if r and h:
                if r.val == h.val:
                    return check(r.left, head.next) or check(r.right, head.next)
                else:
                    return False
            elif h is None:
                return True
            else:
                return False

        def solve(r):
            if r:
                is_present = solve(r.left)
                if is_present:
                    return True
                if not is_present and r.val == head.val and check(r, head):
                    return True
                return solve(r.right)

            
        return solve(root)