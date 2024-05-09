from typing import List


class Solution:

    def dfs(self, root, leftChild, rightChild, visited):
        if root != -1 and root not in visited:
            visited.add(root)
            return self.dfs(
                leftChild[root], leftChild, rightChild, visited
            ) and self.dfs(rightChild[root], leftChild, rightChild, visited)
        elif root == -1:
            return True
        else:
            return False

    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        s = set()
        for index in range(n):
            if leftChild[index] != -1:
                s.add(leftChild[index])
            if rightChild[index] != -1:
                s.add(rightChild[index])

        if len(s) == n - 1:
            for root in range(n):
                if root not in s:
                    break
            visited = set()
            no_back_cycle = self.dfs(root, leftChild, rightChild, visited)
            return no_back_cycle and len(visited) == n

        else:
            return False


print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
