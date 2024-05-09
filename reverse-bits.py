class Solution:
    # def to_binary(self, n:int):
    #     result = []
    #     i = 0
    #     while i < 32:
    #         result.append(n%2)
    #         n = n//2
    #         i += 1
    #     return result

    # def to_decimal(self, n: list):
    #     j = 0
    #     result = 0
    #     while j < len(n):
    #         result += n[j] * (2 ** j)
    #         j += 1
    #     return result

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = result << 1 + n%2
            n >>= 1
        return result
        # bits = self.to_binary(n)
        # bits.reverse()
        # return self.to_decimal(bits)

print(Solution().reverseBits(43261596))
# 00000010100101000001111010011100