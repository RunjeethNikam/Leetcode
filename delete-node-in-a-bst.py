from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def solve(r: TreeNode, k: int):
            if not r:
                return r
            
            if r.val == k:
                if r.right is None:
                    return r.left
                elif r.left is None:
                    return r.right
                else:
                    r_l = r.right.left
                    l = r.left
                    r.left = None
                    r.right.left = l
                    while l.right:
                        l = l.right
                    l.right = r_l
                return r.right

            elif r.val < k:
                r.right = solve(r.right, k)
            else:
                r.left = solve(r.left, k)
            return r

        return solve(root, key)


t = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(54)), TreeNode(6, None, TreeNode(7)))
Solution().deleteNode(t, 3)
