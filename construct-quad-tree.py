from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def validate(self, i, j, grid, n):
        expected = grid[i][j]
        for I in range(i, i + n):
            for J in range(j, j + n):
                if grid[I][J] != expected:
                    return False, 1
        return True, expected

    def const(self, i, j, grid, n):
        # isValid, val = self.validate(i, j, grid, n)
        node: Node
        if n == 1:
            node = Node(grid[i][j], True, None, None, None, None)
        else:
            d = n // 2
            topLeft = self.const(i, j, grid, d)
            topRight = self.const(i, j + d, grid, d)
            bottomLeft = self.const(i + d, j, grid, d)
            bottomRight = self.const(i + d, j + d, grid, d)
            if (
                topLeft.val == topRight.val
                and topRight.val == bottomLeft.val
                and bottomLeft.val == bottomRight.val
                and topLeft.isLeaf
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
            ):
                node = Node(topLeft.val, True, None, None, None, None)
            else:
                node = Node(
                    1,
                    False,
                    topLeft,
                    topRight,
                    bottomLeft,
                    bottomRight,
                )
        return node

    def construct(self, grid: List[List[int]]) -> Node:
        return self.const(0, 0, grid, len(grid))


print(Solution().construct([[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]))
