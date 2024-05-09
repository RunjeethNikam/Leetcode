from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                st.append(token)
            else:
                t2 = int(st.pop())
                t1 = int(st.pop())
                if token == '+':
                    st.append(t1 + t2)
                if token == '-':
                    st.append(t1 - t2)
                if token == '*':
                    st.append(t1 * t2)
                if token == '/':
                    st.append(t1 // t2)
        return st.pop()

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))