from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solv(self, root):
        while root:
            rt = root.right
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = rt
                

        # if root:

        #     if (root.left is None and root.right is None):
        #         return [root, root]


        #     rt = root.right

        #     if root.left:
        #         start, end = self.solv(root.left)
        #         root.left = None
        #         root.right = start
        #         end.right = rt
        #     start, end = self.solv(rt)
        #     return root, end
            

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.solv(root)
        return root
    

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6)))
Solution().flatten(root)
