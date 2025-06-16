class Solution:
    def getSum(self, a: int, b: int) -> int:
        def solve(number, index):
            return bool(number & (1 << index))

        carry = 0
        result = 0
        for i in range(64):
            a_bit = solve(a, i)
            b_bit = solve(b, i)
            if carry == 1:
                if a_bit == 1 and b_bit == 1:
                    result = (1 << i) ^ result
                elif a_bit == 0 and b_bit == 0:
                    carry = 0
                    result = (1 << i) ^ result
                else:
                    pass
            else:
                if a_bit == 1 and b_bit == 1:
                    carry = 1
                elif a_bit == 0 and b_bit == 0:
                    pass
                else:
                    result = (1 << i) ^ result
        return result


print(Solution().getSum(a=1, b=3))
