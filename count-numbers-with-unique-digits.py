class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0, 10, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920]

        return sum(dp[:n+1])
        # dp = [0] * 10
        # dp[1] = 10
        # dp[2] = 81

        # count = 8
        # for i in range(3, 10):
        #     dp[i] = dp[i-1] * count
        #     count -= 1




        print(dp)

print(Solution().countNumbersWithUniqueDigits(10))

        
        