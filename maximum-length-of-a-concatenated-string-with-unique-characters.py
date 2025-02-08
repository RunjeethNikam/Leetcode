from typing import List
from string import ascii_lowercase


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = dict(map(lambda item: (item[1], item[0]), enumerate(ascii_lowercase)))
        result = 0

        def solve(index, selected_alpha):
            if index == len(arr):
                nonlocal result
                result = max(bin(selected_alpha).count('1'), result)
                return
            else:
                solve(index + 1, selected_alpha)
                msk = 0
                for ch in arr[index]:
                    m = 1 << dp[ch]
                    if (msk & m) != 0:
                        return
                    msk = msk | m
                if (msk & selected_alpha) == 0:
                    solve(index + 1, selected_alpha | msk)

        solve(0, 0)
        return result


print(Solution().maxLength(arr=["un", "iq"]))
# 100000010000000000000
# 100000000000000010000
