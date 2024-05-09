class Solution:

    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        c = 0
        st = []

        for i in range(len(s)):
            token = s[i]
            if token in '0123456789':
                c = c*10 + int(token)
            if token in '-+':
                res += sign * c
                c = 0
                sign = -1 if token == '-' else 1
            if token == '(':
                st.append(res)
                st.append(sign)
                res = 0
                sign = 1
            if token == ')':
                res += c * sign
                c = 0
                sign = 1
                res *= st.pop()
                res += st.pop()
        res += sign * c
        return res
    
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))