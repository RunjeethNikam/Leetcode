class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if i == 0 and j == 0:
                    return False
                elif typed[j-1] == typed[j]:
                    j += 1
                else:
                    return False
        while j < len(typed):
            if typed[j] == typed[j-1]:
                pass
            else:
                return False
            j += 1
        return i == len(name)

print(Solution().isLongPressedName("alex", "alexx"))
            