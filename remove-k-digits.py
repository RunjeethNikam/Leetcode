class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st = []
        count = 0
        i = 0
        while i < len(nums):
            nm = nums[i]
            while count < k and st and st[-1] > nm:
                st.pop()
                count += 1
            if st or nm != 0:
                st.append(nm)
            i += 1

        while count < k:
            st.pop()
            count += 1

        return "".join(st) or "0"


print(Solution().removeKdigits("10200", 1))
