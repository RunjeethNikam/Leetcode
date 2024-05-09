class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st = []
        points = {
            'ab': x,
            'ba': y
        }
        if x > y:
            mx = 'ab'
            o = 'ba'
        else:
            mx = 'ba'
            o = 'ab'
        result = 0
        for ch in s:
            st.append(ch)
            if st[-2:] == list(mx):
                result += points[mx]
                st.pop()
                st.pop()
        st1 = []
        for ch in st:
            st1.append(ch)
            if st1[-2:] == list(o):
                result += points[o]
                st1.pop()
                st1.pop()
            # elif len(st) >= 3 and st[-3: -1] == list(o):
            #     result += points[o]
            #     st.pop()
            #     st.pop()
            #     st.pop()
            #     st.append(ch)
        
        # if st[-2:] == list(o) or st[-3: -1] == list(o):
        #     result += points[o]
        return result
    

print(Solution().maximumGain("cdbcbbaaabab", 4, 5))
