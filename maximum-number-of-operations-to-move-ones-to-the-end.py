class Solution:
    def maxOperations(self, s: str) -> int:
        s = s + '1'
        flag = False
        count = 0
        result = 0
        for ch in s:
            if ch == "1" and flag:
                result += count
            if ch == "0":
                flag = True

            if ch == "1":
                count += 1
                flag = False
        return result


print(Solution().maxOperations("00111"))
