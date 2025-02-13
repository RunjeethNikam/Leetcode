from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(left, right):
            if left > right:
                return [None]
            result = []
            for root in range(left, right + 1):
                left_trees = solve(left, root-1)
                right_trees = solve(root + 1, right)
                for lt in left_trees:
                    for rt in right_trees:
                        result.append(
                            TreeNode(root, lt, rt)
                        )
            return result

            
        return solve(1, n)