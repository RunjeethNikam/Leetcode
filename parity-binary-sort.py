t = int(input())
for _ in range(t):
    n = int(input())
    given = map(int, input().split())
    def count(x):
        ones = 0
        temp = x
        while x:
            ones += x%2
            x >>= 1
        return ones%2, temp
    given = list(map(count, given))
    given.sort(key=lambda _: (_[0], _[1]))
    print(list(map(lambda _: _[1], given)))