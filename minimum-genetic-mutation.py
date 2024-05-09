from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if len(startGene) != len(endGene):
            return -1
        bank = set(bank)
        # missing_index = []
        options = ["A", "C", "G", "T"]
        # for index, [a, b] in enumerate(zip(startGene, endGene)):
        #     if a != b:
        #         missing_index.append(index)

        q = deque([[startGene, 0]])
        seen = set()
        while len(q):
            gene, step = q.popleft()
            if gene == endGene:
                return step
            else:
                for index in range(len(startGene)):
                    for ch in options:
                        if ch != gene[index]:
                            new_gene = gene[:index] + ch + gene[index + 1 :]
                            if new_gene not in seen and new_gene in bank:
                                seen.add(new_gene)
                                q.append(
                                    [
                                        new_gene,
                                        step + 1,
                                    ]
                                )
        return -1


print(Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
