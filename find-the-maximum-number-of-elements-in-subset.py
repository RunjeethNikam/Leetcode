from typing import List
from collections import defaultdict
from math import sqrt


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        f = dict()
        for num in nums:
            if num not in f:
                f[num] = 1
            else:
                f[num] += 1
        result = 1
        for key, value in f.items():
            ans = 0
            if key != 1:
                while key in f:
                    if f[key] == 1:
                        ans += 1
                        break
                    elif f[key] >= 2:
                        ans += 2    
                    key = key * key
                if ans > 2:
                    if ans %2 == 1:
                        result = max(result, ans)
                    else:
                        result = max(result, ans-1)
            else:
                if value <= 2:
                    result = max(result, 1)
                else:
                    if value % 2 == 1:
                        result = max(result, value)
                    else:
                        result = max(result, value-1)
        return result
        

print(Solution().maximumLength([1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024]))
