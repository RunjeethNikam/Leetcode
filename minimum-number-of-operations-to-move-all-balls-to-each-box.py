from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        boxes = list(map(int, boxes))
        result = []
        count = 0
        right = 0
        for value in boxes:
            right += count
            result.append(right)
            count += value

        left = 0
        count = 0
        for index in range(len(boxes) - 1, -1, -1):
            left += count
            result[index] += left
            count += boxes[index]
        return result


print(Solution().minOperations("001011"))
