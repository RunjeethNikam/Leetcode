from typing import List


class Solution:
    mp = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: "ghi",
        5: "jke",
        6: "mno",
        7: "pqr",
        8: "tuv",
        9: "wxyz",
    }
    result = []

    def solv(self, i, digits, word):
        if i < len(digits):
            for ch in self.mp[digits[i]]:
                self.solv(i + 1, digits, word + ch)
        else:
            self.result.append(word)

    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.solv(0, digits, "")
        return self.result
