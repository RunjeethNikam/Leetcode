class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        res, i = {}, 0
        h = []
        for p in sorted(people):
            while i < len(flowers) and flowers[i][0] <= p:
                heapq.heappush(h, flowers[i][1])
                i += 1

            while h and h[0] < p:
                heapq.heappop(h)
            res[p] = 0 if not h else len(h)
        return [
            res[p] for p in people
        ]
