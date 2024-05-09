
from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        d = {}
        for i in answers:
            if i == 0:
                result += 1
            else:
                if (i+1) not in d:
                    result += i + 1
                    d[i + 1] = 1
                else:
                    if d[i + 1] == i + 1:
                        d[i + 1] = 0
                        result += i + 1
                    else:
                        d[i + 1] += 1
        return result

        # c = Counter(answers)
        # result = 0
        # for key, value in c.items():
        #     s = value // (key+1)
        #     if value % (key + 1) == 0:
        #         result +=  (s * (key + 1))
        #     else:
        #         result +=  (s * (key + 1)) + (key + 1)
        # return result


print(Solution().numRabbits([10,10,10]))
