class Solution:

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        for i in range(64, -1, -1):
            msk = 1 << i
            if (msk & left) == (msk & right):
                if (msk & left) != 0:
                    result = result | msk
            else:
                return result
        return result


print(Solution().rangeBitwiseAnd(left=1, right=1))
