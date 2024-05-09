class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != num2 and num1 != 1 and num2 != 1:
            if num1 < num2:
                count += num2//num1
                num2 = num2 % num1
            else:
                count += num1//num2
                num1 = num1 % num2

        if num1 == num2:
            count += 1
        elif num1 == 1 or num2 == 1:
            count += max(num1, num2)
        return count