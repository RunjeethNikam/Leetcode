from typing import List
from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        result = 0
        for (X, Y) in self.points.keys():
            if X == x or Y == y or abs(X - x) != abs(Y - y):
                continue
            if (X,y) in self.points and (x,Y) in self.points:
                result += self.points[(X,Y)] * self.points[(x,Y)] * self.points[(X,y)]
        return result



# Simulation of the input commands
# Simulation of the input commands
# Simulation of the input commands
commands = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
values = [
    [],
    [[3, 10]],
    [[11, 2]],
    [[3, 2]],
    [[11, 10]],
    [[14, 8]],
    [[11, 2]],
    [[11, 10]],
]

# Result list to store output of each command
results = []

obj = None

for cmd, val in zip(commands, values):
    if cmd == "DetectSquares":
        obj = DetectSquares()
        results.append(None)
    elif cmd == "add":
        obj.add(val[0])
        results.append(None)
    elif cmd == "count":
        res = obj.count(val[0])
        results.append(res)

print(results)
