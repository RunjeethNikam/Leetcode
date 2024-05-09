class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        limit = 1
        def solve(index):
            nonlocal limit
            if index < len(preorder) and preorder[index] == '#':
                return True
            if limit < len(preorder):
                if preorder[limit] != '#':
                    limit += 1
                    r = solve(limit-1)
                    if not r:
                        return False
                else:
                    limit += 1
            else:
                return False
            if limit < len(preorder):
                if preorder[limit] != '#':
                    limit += 1
                    return solve(limit-1)
                else:
                    limit += 1
                    return True
            else:
                return False
                
        return solve(0) and limit == len(preorder)

    

print(Solution().isValidSerialization('#'))
        