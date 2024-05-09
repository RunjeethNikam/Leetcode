class Solution:

    # def max(self, position):
    #     return 1<<(position+1)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        for i in range(32, -1, -1):
            if (left & (1 << i)) != (right & (1 << i)):
                break
            else:
                result += left & (1<<i)
        return result
    

print(Solution().rangeBitwiseAnd(5,7))