class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = [0] * len(s)
        a = [0] * len(s)
        count = 0
        for index, value in enumerate(s):
            b[index] = count
            if value == "b":
                count += 1
        count = 0
        for index in range(len(s) - 1, -1, -1):
            value = s[index]
            a[index] = count
            if value == "a":
                count += 1
        result = float('inf')
        for i, j in zip(a, b):
            result = min(result, i + j)
        return result
    
print(Solution().minimumDeletions("aababbab"))
