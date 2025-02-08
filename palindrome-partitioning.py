from typing import *
from itertools import product, combinations


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def check_palindrome(given):
            return given == given[::-1]

        def solve(index, path: list):
            if index < len(s):
                for limit in range(index, len(s)):
                    if check_palindrome(s[index : limit + 1]):
                        path.append(s[index : limit + 1])
                        solve(limit + 1, path)
                        path.pop()

            elif path:
                result.append(path[:])

        solve(0, [])
        return result


print(Solution().partition("aab"))
