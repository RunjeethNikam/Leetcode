class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        visited = set()
        for index, ch in enumerate(s):
            if ch not in visited:
                while st and st[-1] > ch and st[-1] in s[index + 1 :]:
                    visited.remove(st[-1])
                    st.pop()
                st.append(ch)
                visited.add(ch)
        return ''.join(st)


print(Solution().smallestSubsequence("cbacdcbc"))
