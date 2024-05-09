from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry = 1
        while i >= 0:
            digits[i] += carry
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
            i -= 0
        if carry == 1:
            digits.insert(0, carry)
        return digits
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     digits.reverse()
    #     carry = 1
    #     i = 0
    #     while i < len(digits):
    #         digits[i] += carry
    #         if digits[i] == 10:
    #             carry = 1
    #             digits[i] = 0
    #     if carry == 1:
    #         digits.append(carry)
    #     digits.reverse()
    #     return digits
