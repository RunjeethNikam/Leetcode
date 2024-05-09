# def func19(n):
#     sequence = [n]
#     count = 0
#     while n > 1:
#         if n % 2 == 1:
#             n = 3 * n + 1
#         else:
#             n = n // 2
#         sequence.append(n)
#         count += 1
#     return ' -> '.join(map(str, sequence)), count

# print(func19(16))
def func(A, x):
    A.sort()
    result = []
    Mystery(A, x, 0, [], result)
    return result

count = 0

def Mystery(A, x, start, p, result):
    global count
    count += 1
    if x == 0:
        result.append(p)
        return
    if x < 0:
        return
    for i in range(start, len(A)):

        Mystery(A, x - A[i], i + 1, p + [A[i]], result)

for i in range(1,30):
    arr = [1] * i
    count = 0
    func(arr, 100)
    print(count, 2 ** len(arr))


[1,1,1,1,1,1,1,1,1], 100
