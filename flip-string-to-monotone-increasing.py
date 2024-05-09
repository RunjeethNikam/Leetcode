class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_zeros = s.count('0')
        count_ones = 0

        result = float("inf")
        for ch in s:
            if ch == '0':
                count_zeros -= 1
            if count_ones + count_zeros < result:
                result = count_ones + count_zeros
            if ch == '1':
                count_ones += 1

        return result


print(Solution().minFlipsMonoIncr("11011"))
