def check(given, mid, diff, y):
    count = 0
    for i in range(len(given)):
        given[i] -= y * mid
        while given[i] > 0:
            given[i] -= diff
            count += 1
    return count <= mid


def function(given, x, y):
    low = 1
    high = 100000000
    while low <= high:
        mid = (low + high) // 2
        if check(given[:], mid, x - y, y):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


print(function([7, 6, 4, 3, 1, 3], 4, 2))
