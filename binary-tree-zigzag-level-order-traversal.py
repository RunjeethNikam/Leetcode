from typing import Optional, List
from collections import de


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        flag = False
        result = []
        while len(q):
            if flag:
                it = iter(q)
            else:
                it = reversed(q)
            r = []
            qq = []
            for item in it:
                r.append(item.val)
                if item.left:
                    qq.append(item.left)
                if item.right:
                    qq.append(item.right)
            result.append(r)
            q = qq
        return result
                    
