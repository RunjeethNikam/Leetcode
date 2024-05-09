from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1, n]
        s = set(result)
        count = n
        while n > 0:
            sm = result[0] + result[-1]
            if sm == 2:
                pass
            elif (sm % 2) == 1:
                pass
            else:
                pass

        