from bisect import *

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    given = list(map(int, input().split()))
    # roots = [num ** (1 / (index + 1)) for index, num in enumerate(given)]
    roots = given[:]
    roots.sort()
    count = sum(
        [bisect(roots, num ** (1 / (index + 1))) for index, num in enumerate(given)]
    )
    print(count)
