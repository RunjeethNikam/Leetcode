from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        q.append(None)
        result = []
        prev = -1
        while len(q):
            item = q.popleft()
            if item:
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            elif len(q):
                result.append(prev.val)
                q.append(item)
            else:
                result.append(prev.val)
            prev = item
        return result