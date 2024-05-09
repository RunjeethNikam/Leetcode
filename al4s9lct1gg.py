from pprint import pprint

# def calculateWays(wordLen, maxVowels):
#     dp = [[0] * (maxVowels+1) for _ in range(wordLen+1)]
#     for i in range(1, wordLen+1):
#         dp[i][0] = 21 ** i
#     for l in range(wordLen+1):
#         for v in range(1, maxVowels+1):
#             if v <= l:
#                 result = 0
#                 for lv in range(0, v+1):
#                     if lv == v:
#                         a = 5**lv
#                         b = 1
#                         c = 1
#                     else:
#                         a = 5**lv
#                         b = 21
#                         c = (dp[l-lv][maxVowels-lv] if dp[l-lv][maxVowels-lv] != 0 else 1)

#                     result += a * b * c
#                 dp[l][v] = result
#             else:
#                 dp[l][v] = dp[l][v-1]
#     pprint(dp)


def calculateWays(wordLen, maxVowels):
    MOD = 10**9 + 7
    dp = [[1] * (maxVowels + 1) for _ in range(wordLen + 1)]
    for i in range(1, wordLen + 1):
        dp[i][0] = (21**i) % MOD
    for l in range(1, wordLen + 1):
        for mx in range(1, maxVowels + 1):
            if mx > l:
                dp[l][mx] = dp[l][mx - 1]
            else:
                result = 0

                for m in range(mx + 1):
                    if m == 0:
                        result += (dp[l - 1][mx] * 21) % MOD
                    elif m == l:
                        result += (5**l) % MOD
                    else:
                        result += (dp[l - m - 1][mx] * 21 * (5**m)) % MOD

                dp[l][mx] = result % MOD
    print(dp[-1][-1] % MOD )


calculateWays(1000, 1000)
