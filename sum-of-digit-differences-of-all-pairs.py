from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        dp = [{} for i in range(11)]
        nums.sort()
        result = 0
        for num in nums:
            position = 0
            while num:
                last = num % 10
                for key, value in dp[position].items():
                    if key != last:
                        result += value
                if last in dp[position]:
                    dp[position][last] += 1
                else:
                    dp[position][last] = 1
                num //= 10
                position += 1
        return result


print(Solution().sumDigitDifferences(nums = [10,10,10,10]))
