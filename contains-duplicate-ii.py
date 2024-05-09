from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        fq = defaultdict(lambda : defaultdict(int))
        for index, value in enumerate(nums):
            fq[value][index] += 1
        for key, value in fq.items():
            if len(value)> 1:
                for key in value.keys():
                    value[key] -= 1
                    if (abs(k-key) in value and value[abs(k-key)]) or (k-key) in value and value[k-key]:
                        return True
                    value[key] += 1
        return False
    
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))