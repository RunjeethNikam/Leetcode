from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = formula[::-1]
        st = []
        d = defaultdict(int)
        i = 0
        while i < len(formula):
            if len(st) == 0 or formula[i] == '(':
                st.append()
                