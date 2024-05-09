from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        q.append(None)
        result = []
        while len(q):
            item = q.popleft()
            result.append(item.val)
            if item:
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            elif len(q):
                q.append(item)
        return result