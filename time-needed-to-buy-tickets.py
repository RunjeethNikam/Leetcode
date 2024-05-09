from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        lt = tickets[k]
        for index, ticket in enumerate(tickets):
            if index <= k:
                count += min(ticket, lt)
            else:
                count += min(ticket, lt-1)
        return count
    

# print(Solution().timeRequiredToBuy([1,2,3,4,2,4,3,2,1], 4))
print(Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))