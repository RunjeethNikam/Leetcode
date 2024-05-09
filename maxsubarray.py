def kadane(arr):
    cs = gs = arr[0]
    for i in range(1, len(arr)):
        cs = max(arr[i], arr[i]+cs)
        gs = max(gs, cs)
    return gs

def has_positive(arr):
    for i in arr:
        if i > 0:
            return True
    return False

def maxSubarray(arr):
    if has_positive(arr):
        return kadane(arr), sum(filter(lambda _: _ > 0, arr))
    else:
        mn = max(arr)
        return mn, mn

print(maxSubarray([-2, -3, -1, -4, -6]))