class Solution:

    def get_index(self, a, i):
        if i < 0:
            return '0'
        else:
            return a[i]
        
    def add(self, a, b, c):
        count = 0
        if a == '1':
            count += 1
        if b == '1':
            count += 1
        if c == '1':
            count += 1
        if count == 3:
            return '1', '1'
        elif count == 2:
            return '1', '0'
        elif count == 1:
            return '0', '1'
        return '0', '0'

    def addBinary(self, num1: str, num2: str) -> str:
        carry = '0'
        i = len(num1) - 1
        j = len(num2) - 1
        result = ''
        while i >= 0 or j >= 0:
            a = self.get_index(num1, i)
            b = self.get_index(num2, j)
            carry, value = self.add(a, b, carry)
            result += value
            i -= 1
            j -= 1
        if carry == "1":
            result += carry
        return result[::-1]
    

print(Solution().addBinary('1010', '1011'))
