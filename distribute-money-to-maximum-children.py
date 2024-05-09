class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children * 8 < money:
            return children - 1
        elif children * 8 == money:
            return children
        else:
            if money < (children + 7):
                if money >= children:
                    return 0
                else:
                    return -1
            else:
                count = 0
                children_remaining = children
                remaining_money = money
                while children_remaining > 0:
                    if remaining_money >= (children_remaining + 7):
                        count += 1
                        remaining_money -= 8
                    else:
                        if remaining_money == 4 and children_remaining == 1:
                            count -= 1
                        break
                    children_remaining -= 1
        return count
    
print(Solution().distMoney(17, 3))

# 17, 3
# 8, 8, 1
