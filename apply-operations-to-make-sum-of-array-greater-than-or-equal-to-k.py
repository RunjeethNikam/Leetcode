class Solution:
    def minOperations(self, k: int) -> int:
        result = 1
        flag = True
        sm = 1
        step = 0
        while True:
            if sm >= k:
                break
            if flag:
                result += 1
                sm += 1
            else:
                sm += result
            flag = not flag
            step += 1
        return step

print(Solution().minOperations(3))