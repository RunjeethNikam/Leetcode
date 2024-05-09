from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        def solve(lt, l):
            low = 0
            high = len(lt) - 1
            while low <= high:
                mid = (high + low) // 2
                if lt[mid] <= l:
                    low = mid + 1
                else:
                    high = mid - 1
            return lt[low] if low < len(lt) else float('inf')

        df = defaultdict(list)
        for index, ch in enumerate(s):
            # if ch not in df:
            df[ch].append(index)
        
        count = 0
        for word in words:
            last = -1
            for ch in word:
                last = solve(df[ch], last)
                if last == float('inf'):
                    break
            else:
                count += 1
        return count

print(Solution().numMatchingSubseq("dsahjpjauf",["ja","ahjpjau","ahbwzgqnuk","tnmlanowax"]))