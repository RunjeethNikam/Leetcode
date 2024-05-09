def Missingsmallest(A, low, high):
    if low > high:
        return low
    mid = (high + low) // 2
    if A[mid] > mid:
        return Missingsmallest(A, low, mid - 1)
    else:
        return Missingsmallest(A, mid + 1, high)


print(Missingsmallest([0, 1, 2, 3, 4, 5, 6, 7, 9], 0, 8))


# Questions to the professor
# DNC
# question 7
# white black pair problem
# large integer multiplication
# Greedy
# what types of questions can we expect for huffman coding