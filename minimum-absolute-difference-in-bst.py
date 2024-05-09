from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # counter = 0

    # def solve(self, root, k):
    #     if root:
    #         val = self.solve(root.left)
    #         if not val:
    #             self.counter += 1
    #             if self.counter == k:
    #                 return root.val
    #         else:
    #             return val
    #         return self.solve(root.right)



    def getMinimumDifference(self, root: Optional[TreeNode], k) -> int:
        cur = root
        counter = 0
        while cur:
            if cur.left:
                l = cur.left
                while l and l.right and l.right != cur:
                    l = l.right
                if l.right == cur:
                    l.right = None
                    counter += 1
                    if counter == k:
                        return cur.val
                    cur = cur.right
                else:
                    l.right = cur
                    cur = cur.left