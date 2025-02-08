from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = deque()
        st = []
        count = 0
        wd = deque()
        flag = True
        for ch in s:
            if ch == "(":
                count += 1
                flag = False
                st.append("".join(wd))
                wd.clear()
            elif ch == ")":
                count -= 1
                if flag:
                    result.appendleft(st.pop())
                    result.append("".join(wd))
                else:
                    flag = True
                    result.append("".join(wd))
                wd.clear()
            else:
                if count % 2 == 1:
                    wd.append(ch)
                else:
                    wd.appendleft(ch)

        return "".join(result)[::-1]


print(Solution().reverseParentheses("(ed(et(oc))el)"))
