class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            if not st:
                st.append(ch)
            else:
                if (ch.isupper() and ch.lower() == st[-1]) or (ch.islower() and ch.upper() == st[-1]):
                    st.pop()
                else:
                    st.append(ch)
        return ''.join(st)


a, A
