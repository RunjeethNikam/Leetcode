from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ordering = defaultdict(list)
        def dfs(root, row, col):
            if root:
                ordering[col].append((row, root.val))
                dfs(root.left, row + 1, col - 1)
                dfs(root.left, row + 1, col + 1)
        dfs(root, 0, 0)
        mn_col = min(ordering.keys())
        result = []
        while mn_col in ordering:
            result.append(map(lambda item: item[1], sorted(ordering[mn_col])))
            mn_col += 1
        return result
                
