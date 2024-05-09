# from string import alpha


class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        i  = 0
        while i < len(s):
            if s[i] == '[':
                st.append('[')
                i += 1
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                st.append(num)
            elif s[i].isalpha():
                result = ""
                while i < len(s) and s[i].isalpha():
                    result = result + s[i]
                    i += 1
                st.append(result)
            else:
                top = ""
                while st[-1] != '[':
                    top = st.pop() + top
                st.pop()
                num = st.pop() * top
                st.append(num)
                i += 1 

        return "".join(st)

    

print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))

