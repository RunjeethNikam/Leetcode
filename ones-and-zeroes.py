from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def solve(index, current_m, current_n, count):
            if index == len(strs):
                return count
            else:
                # not select
                mx = solve(index + 1, current_m, current_n, count)
                # select
                current_m += strs[index].count("0")
                current_n += strs[index].count("1")
                if current_n <= n and current_m <= m:
                    mx = max(mx, solve(index + 1, current_m, current_n, count + 1))
                return mx

        return solve(0, 0, 0, 0)

        # lnt = len(strs)
        # dp = [[0, 0, 0] for _ in range(lnt + 1)]
        # for i in range(1, lnt + 1):
        #     current_zeros = strs[i - 1].count("0")
        #     current_ones = len(strs[i - 1]) - current_zeros
        #     for j in range(i):
        #         prev_zeros, prev_ones, count = dp[j]
        #         if (
        #             (current_zeros + prev_zeros) <= m
        #             and (current_ones + prev_ones) <= n
        #             and (count + 1) > dp[i][2]
        #         ):
        #             dp[i] = [
        #                 (current_zeros + prev_zeros),
        #                 (current_ones + prev_ones),
        #                 count + 1,
        #             ]
        # return max(dp, key=lambda item: item[-1])[-1]


print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
