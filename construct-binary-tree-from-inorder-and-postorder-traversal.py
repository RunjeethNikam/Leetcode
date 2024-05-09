from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexes = {value: index for index, value in enumerate(inorder)}

        def solve(low, high, i, j):
            if low <= high and i <= j:
                root = TreeNode(postorder[high])
                root_index = indexes[postorder[high]]
                left_elements = j - root_index
                root.left = solve(
                    low, high - 1 - left_elements, i, root_index-1
                )
                root.right = solve(high - left_elements, high-1, root_index+1, j)
                return root
        return solve(0, len(inorder)-1, 0, len(inorder)-1)
