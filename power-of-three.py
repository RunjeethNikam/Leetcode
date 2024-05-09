import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x =math.log(n) / math.log(3)
        print(x)
        return int(x) == x
        
print(Solution().isPowerOfThree(4782968))