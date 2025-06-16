class Solution:

    def solve(self, q, indexes):
        if len(indexes) == 1:
            return -1
        index = bisect(indexes, q)
        return min(
            indexes[index + 1] - indexes[index], indexes[index] - indexes[index - 1]
        )

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dp = defaultdict(list)
        for index, num in enumerate(nums):
            dp[num].append(index)
        for _, value in dp.items():
            if len(value) > 1:
                value.append(value[0] + len(nums))
                value.insert(0, value[-2] - len(nums))
        result = []
        for q in queries:
            result.append(self.solve(q, dp[nums[q]]))
