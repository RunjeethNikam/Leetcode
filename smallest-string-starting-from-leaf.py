from typing import Optional
from typing import Optional
from string import ascii_lowercase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mn = 'z' * 30
        def solve(r, p):
            if r:
                current_ch = ascii_lowercase[r.val]
                if not (r.left or r.right):
                    mn = min(mn, p + current_ch)
                solve(r.left, p + current_ch)
                solve(r.right, p + current_ch)

        solve(root, "")
        return mn

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

# root = TreeNode(25)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(2)

print(Solution().smallestFromLeaf(root))