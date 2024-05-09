from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        d = 0
        result = [0] * len(deck)
        q = deque(range(len(deck)))
        while len(q):
            index = q.popleft()
            result[index] = deck[d]
            d += 1
            if q:
                q.append(q.popleft())
        return result


print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
