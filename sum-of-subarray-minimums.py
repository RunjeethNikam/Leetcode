from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result 

# from typing import List


# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         left = [-1] * len(arr)
#         right = [len(arr)] * len(arr)

#         st = []
#         for index, value in enumerate(arr):
#             while st and arr[st[-1]] >= value:
#                 st.pop()
#             if st:
#                 left[index] = st[-1]
#             st.append(index)
        


#         st = []
#         for index in range(len(arr)-1, -1, -1):
#             value = arr[index]
#             while st and arr[st[-1]] >= value:
#                 st.pop()
#             if st:
#                 right[index] = st[-1]
#             st.append(index)
        
#         print(left, right)
#         result = 0
#         for i, l, r in zip(range(len(arr)), left, right):
#             result += ((i-l) * (r - i)) * arr[i]
#         return result


print(Solution().sumSubarrayMins([1,1,1,1]))

