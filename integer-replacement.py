class Solution:
    def integerReplacement(self, n: int) -> int:
        d = {1: 0}

        def dfs(c: int):
            if c in d:
                return d[c]
            else:
                mn = None
                if (c % 2) == 0:
                    mn = dfs(c // 2) + 1
                else:
                    mn = min(dfs(c - 1), dfs(c + 1)) + 1
                d[c] = mn
                return mn
        
        return dfs(n)
    

print(Solution().integerReplacement(7))
