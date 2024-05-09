def substrings(n):
    dp = [0 for _ in range(len(n))]
    for index, value in enumerate(n):
        if index == 0:
            dp[index] = int(value)
        else:
            dp[index] = dp[index-1] * 10 + int(value) * (index+1)
    print(dp)
    return sum(dp)

print(substrings('123'))