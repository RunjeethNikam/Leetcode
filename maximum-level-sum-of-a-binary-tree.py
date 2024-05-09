from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        s = [root]
        mx_sm = float('-inf')
        level = None
        curr_level = 1
        while len(s):
            nxt_level = []
            curr_sm = 0
            for r in s:
                curr_sm += r.val
                if r.left:
                    nxt_level.append(r.left)
                if r.right:
                    nxt_level.append(r.right)
            s = nxt_level
            
            if curr_sm > mx_sm:
                mx_sm = curr_sm
                level = curr_level
            curr_level += 1
        return level