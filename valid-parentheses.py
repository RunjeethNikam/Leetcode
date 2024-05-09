class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        opening_b = ['(', '[', '{']
        closeing_mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for item in s:
            if not st or item in opening_b:
                st.append(item)
            else:
                if item in closeing_mapping and st[-1] != closeing_mapping[item]:
                    return False
                if item in closeing_mapping and st[-1] == closeing_mapping[item]:
                    st.pop()
        return True