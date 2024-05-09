from typing import Optional, List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        s: Dict[int, int] = {0: 1}
        def solve(r: TreeNode, curr_sum: int):
            nonlocal result
            nonlocal s
            if r:
                curr_sum += r.val
                if (curr_sum - targetSum) in s:
                    result += s[curr_sum - targetSum]
                if curr_sum in s:
                    s[curr_sum] += 1
                else:
                    s[curr_sum] = 1
                solve(r.left, curr_sum)
                solve(r.right, curr_sum)
                s[curr_sum] -= 1
                if s[curr_sum] == 0:
                    del s[curr_sum]
        solve(root, 0)
        return result