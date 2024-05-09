N = int(input())
A = map(int, input().split())
mp = {}
for index, a in enumerate(A):
    if (a - index) in mp:
        mp[a-index] += 1
    else:
        mp[a-index] = 1

result = 0

for key, value in mp.items():
    if value > 1:
        result += (value * (value + 1))//2
    
print(result)