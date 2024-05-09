def countArray(n, k, x):
    if x == 1:
        t = 1
        p = 0
    else:
        t = 0
        p = 1
    dp = [[t, p] for _ in range(n)]
    for index in range(1, n):
        if index != n-2:
            dp[index][0] = dp[index-1][1]
            dp[index][1] = dp[index-1][0] * (k-1) + dp[index-1][1] * (k-2)
        else:
            print(dp)
            return dp[index-1][0] * (k-1) + dp[index-1][1] * (k-2)


print(countArray(3, 4, 1))