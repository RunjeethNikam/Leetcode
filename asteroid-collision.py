from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        i = 0
        while i < len(asteroids):
            value = asteroids[i]
            if len(s) == 0:
                s.append(value)
                i += 1
            elif s[-1] * value > 0:
                s.append(value)
                i += 1
            elif value > 0:
                s.append(value)
                i += 1
            else:
                if abs(s[-1]) == abs(value):
                    s.pop()
                    i += 1 
                elif s[-1] > abs(value):
                    i += 1
                else:
                    s.pop()
        return s
    
print(Solution().asteroidCollision([10,2,-5]))
