class Solution:
    def numSteps(self, s: str) -> int:
        lt_s = list(s)

        while lt_s or (len(lt_s) != 1 and lt):
            if lt_s[-1] == '0':
                lt_s.pop()
            else:
                pass
        # s = int(s, 2)
        # count = 0
        # while s != 1:
        #     if s % 2 != 1:
        #         s = s // 2
        #     else:
        #         s += 1
        #     count += 1
        # return count


print(Solution().numSteps(s="1101"))
