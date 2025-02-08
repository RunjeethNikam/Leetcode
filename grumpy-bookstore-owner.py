from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        sm = sum(
            map(lambda item: item[0] if item[1] == 0 else 0, zip(customers, grumpy))
        )

        low = 0
        g = 0
        result = 0
        for high in range(len(customers)):
            if grumpy[high] == 1:
                g += customers[high]
            while (high - low + 1) > minutes:
                if grumpy[low] == 1:
                    g -= customers[low]
                low += 1
            result = max(result, sm + g)
        return result


print(Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1))


# [1,0,1,2,1,1,7,5]
# [0,1,0,1,0,1,0,1]
