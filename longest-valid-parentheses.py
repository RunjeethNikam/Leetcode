class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [(None, -1)]
        result = 0
        for index, ch in enumerate(s):
            if ch == ")" and st[-1][0] == "(":
                result = max(result, index - st[-2][1])
                st.pop()
            else:
                st.append((ch, index))
        return result


print(Solution().longestValidParentheses("(()("))
