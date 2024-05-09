from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        q.append(None)
        sm = 0
        count = 0
        result = []

        while len(q):
            item = q.popleft()
            count += 1
            sm += item.val
            if not item and len(q):
                result.append(sm/count)
                sm = 0
                count = 0
                q.append(item)
            elif item:
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
        return result

        