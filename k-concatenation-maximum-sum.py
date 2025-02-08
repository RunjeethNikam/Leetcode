from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadans(arr):
            start = None
            end = None
            total_sum = float("-inf")
            current_sum = 0
            s = 0
            for index, value in enumerate(arr):
                current_sum += value
                if current_sum > total_sum:
                    total_sum = current_sum
                    start = s
                    end = index
                if current_sum < 0:
                    current_sum = 0
                    s = index + 1
            if end is None and start is not None:
                end = index
            return start, end, total_sum

        if k > 1:
            s, e, sm = kadans(arr + arr)
        else:
            s, e, sm = kadans(arr)
            if sm <= 0:
                return 0
            else:
                return sm % MOD
        if sm <= 0:
            return 0
        else:
            ln = e - s + 1
            if ln >= len(arr):
                return (sm % MOD + (sum(arr) * (k - 2)) % MOD) % MOD
            else:
                return sm % MOD


print(Solution().kConcatenationMaxSum(arr=[-1], k=1))
