from typing import List
from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x -= 1
        y -= 1
        q = deque()
        visited = set()
        result = [0 for _ in range(n)]
        for node in range(0, n):
            q.append((node, 0))
            while len(q):
                node_number, distance = q.popleft()
                # if node_number not in visited:
                visited.add(node_number)
                if distance != 0:
                    result[distance-1] += 1
                if node_number < n-1 and (node_number + 1) not in visited:
                    visited.add(node_number + 1)
                    q.append((node_number + 1, distance + 1))
                if node_number > 0 and (node_number - 1) not in visited:
                    visited.add(node_number - 1)
                    q.append((node_number - 1, distance + 1))
                if node_number == x and y not in visited:
                    visited.add(y)
                    q.append((y, distance + 1))
                if node_number == y and x not in visited:
                    visited.add(x)
                    q.append((x, distance + 1))
            visited.clear()
        return result

print(Solution().countOfPairs(3, 1, 3))