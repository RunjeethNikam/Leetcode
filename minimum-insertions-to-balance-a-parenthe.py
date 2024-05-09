class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        for ch in s:
            if ch == ')' and st[-2:] == list('()'):
                st.pop()
                st.pop()
                continue
            s.append(ch)
        result = 0
        while st:
            if st[-2:] == list('()'):
                st.pop()
                st.pop()
                result += 1
            elif st[-2:] == list('))'):
                st.pop()
                st.pop()
            elif st[-2: ] == list('(('):
                result += 1
                st.pop()
                st.pop()
            elif st[-1] == '(':
                result += 2
                st.pop()
            else: # st[-1] == ')':
                st.pop()
                result += 2