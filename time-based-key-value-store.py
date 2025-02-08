from collections import defaultdict
from bisect import *


class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lt = self.cache[key]
        index = bisect(lt, timestamp, key=lambda item: item[0])
        if index > 0:
            return lt[index - 1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
print(obj.get("love", 5))
