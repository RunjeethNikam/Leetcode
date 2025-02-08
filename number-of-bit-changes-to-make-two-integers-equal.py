class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        b_n = bin(n)[2:]
        b_k = bin(k)[2:]
        max_len = max(len(b_n), len(b_k))
        b_n = b_n.rjust(max_len, "0")
        b_k = b_k.rjust(max_len, "0")
        count = 0
        for i, j in zip(b_n, b_k):
            if i != j and i == "0":
                return -1
            if i != j and i == "1":
                count += 1
        return count


print(Solution().minChanges(44, 2))
