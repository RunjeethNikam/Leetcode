from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        # diff = len(version1) - len(version2)
        # if diff > 0:
        #     version2 = [0] * abs(diff) + version2
        # elif diff < 0:
        #     version1 = [0] * abs(diff) + version1

        # print(version1, version2)

        for v1, v2 in zip_longest(version1, version2, fillvalue='0'):
            v1 = int(v1)
            v2 = int(v2)
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            else:
                continue
        return 0

print(Solution().compareVersion('0.1', "1.1"))
