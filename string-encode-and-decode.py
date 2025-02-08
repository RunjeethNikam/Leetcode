from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#")
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            num = 0
            while i < len(s) and s[i] != "#":
                num = num * 10 + int(s[i])
                i += 1
            i += 1
            st = []
            for _ in range(num):
                st.append(s[i])
                i += 1
            result.append("".join(st))
        return result


print(Solution().decode(Solution().encode(["neet", "code", "love", "you"])))
