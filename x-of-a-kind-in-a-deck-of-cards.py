from typing import List
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        f = [0 for i in range(max(deck) + 1)]
        for num in deck:
            f[num] += 1

        ls = None
        for freq in f:
            if freq != 0 and freq > 1:
                if ls is None:
                    ls = freq
                    continue

                ls = math.gcd(freq, ls)
                if ls == 1:
                    return False
            elif freq == 1:
                return False
        return True
    
print(Solution().hasGroupsSizeX([1,1,1,1, 2,2,2,2,2,2]))
print(Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(Solution().hasGroupsSizeX([1]))
print(Solution().hasGroupsSizeX([1,1,2,2,2,2]))
