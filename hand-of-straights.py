from collections import Counter
from typing import List
from heapq import *


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        min_heap = list(c.items())
        heapify(min_heap)
        while len(min_heap) >= groupSize:
            group = []
            extra = []
            for _ in range(groupSize):
                card, freq = heappop(min_heap)
                if freq != 1:
                    extra.append((card, freq - 1))
                if not group or group[-1] + 1 == card:
                    group.append(card)
                else:
                    return False
            for card, freq in extra:
                heappush(min_heap, (card, freq))
        return len(min_heap) == 0


print(Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
