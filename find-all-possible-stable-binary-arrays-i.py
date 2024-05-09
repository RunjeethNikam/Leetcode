def count_stable_arrays(zero, one, limit):
    MOD = 10**9 + 7

    # Initialize the DP array
    dp = [[0] * (one + 1) for _ in range(zero + 1)]
    dp[0][1] = 1  # Initialize the case where the first element is 1

    # Iterate through each possible length of the array
    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            # If we add a 0, we can keep the number of ones or decrease it by 1
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

            # If the length exceeds limit, we need to make sure the last subarray contains both 0 and 1
            if i > limit:
                dp[i][j] = (dp[i][j] + dp[i - limit - 1][j - 1]) % MOD

    return dp[zero][one]

# Example usage
zero = 1
one = 1
limit = 2
print(count_stable_arrays(zero, one, limit))  # Output should be 1
