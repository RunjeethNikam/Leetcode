from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def solve(path, remaining, flag):
            if remaining > 0:
                solve(path + "1", remaining - 1, True)
                if flag:
                    solve(path + "0", remaining - 1, False)
            else:
                result.append(path)

        solve("", n, True)

        return result


print(Solution().validStrings(3))
