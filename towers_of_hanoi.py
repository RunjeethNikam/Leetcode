
count = 0

def hanoi(pegs, source, aux, target):
    global count
    if pegs == 1:
        count += 1
        # print(f"Move {source} to {target}")
        return 
    hanoi(pegs-1, source, target, aux)
    # print(f"Move {source} -> {target}")
    count += 1
    hanoi(pegs-1, aux, source, target)

# hanoi(2, 'A', 'B', 'C')
# print(count)

def hanoi_dp(pegs):
    dp = [0 for _ in range(pegs+2)]
    dp[1] = 1
    for i in range(1, pegs+1):
        dp[i] = 2*dp[i-1] + 1
    return dp[pegs]

# hanoi(2, 'A', 'B', 'C')
# print(count)
# print(hanoi_dp(2))

# count = 0
# hanoi(3, 'A', 'B', 'C')
# print(count)
# print(hanoi_dp(3))

# count = 0
# hanoi(4, 'A', 'B', 'C')
# print(count)
# print(hanoi_dp(4))

# count = 0
# hanoi(5, 'A', 'B', 'C')
# print(count)
# print(hanoi_dp(5))


count = 0
hanoi(11, 'A', 'B', 'C')
print(count)
print(hanoi_dp(11))


# for i in range(4):
#     count = 0
#     hanoi(i, 'A', 'B', 'C')
#     print(count == hanoi_dp(i))

# print(hanoi_dp(2))


    