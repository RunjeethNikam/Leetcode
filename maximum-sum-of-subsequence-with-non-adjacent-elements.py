from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], 0)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.merge(
                self.tree[left_child], self.tree[right_child], start == end - 1
            )

    def merge(self, left, right, level_1):
        # if level_1:
        #     return (right[0], left[0])
        # else:
        #     return (
        #         left[1],
        #     )
        include = max(left[1] + right[0], left[0], right[1])
        exclude = max(left[1], right[1])
        return (include, exclude)

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = (value, 0)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def update_value(self, idx, value):
        self.update(idx, value, 0, 0, self.n - 1)

    def query(self):
        return self.tree[0][0]


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        segment_tree = SegmentTree(nums)
        print(segment_tree.query())
        # result = []
        # for idx, value in queries:
        #     segment_tree.update_value(idx, value)
        #     print(segment_tree.query())


Solution().maximumSumSubsequence(nums=[3, 5, 9], queries=[[1, -2], [0, -3]])
