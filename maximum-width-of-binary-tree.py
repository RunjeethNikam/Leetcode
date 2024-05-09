from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        result = 1
        while len(q):
            for _ in range(len(q)):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, index * 2))
                if node.right:
                    q.append((node.right, (index * 2) + 1))
            result = max(result, q[-1] - q[0] + 1)

        return result


t = TreeNode(
    1,
    TreeNode(3, TreeNode(5, TreeNode(6))),
    TreeNode(2, None, TreeNode(9, TreeNode(7))),
)

print(Solution().widthOfBinaryTree(t))
