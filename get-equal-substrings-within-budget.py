from string import ascii_lowercase


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_mapping = dict(zip(ascii_lowercase, range(26)))
        print(cost_mapping)
        start = None
        end = None
        cost = 0
        result = 0
        for index, [i, j] in enumerate(zip(s, t)):
            if start is None:
                start = end = index
                cost = abs(cost_mapping[i] - cost_mapping[j])
            else:
                cost += abs(cost_mapping[i] - cost_mapping[j])
                end = index
                while start <= end and cost > maxCost:
                    cost -= abs(cost_mapping[s[start]] - cost_mapping[t[start]])
                    start += 1
            if cost <= maxCost:
                result = max(result, end - start + 1)
        return result


print(Solution().equalSubstring(s="pxezla", t="loewbi", maxCost=25))
