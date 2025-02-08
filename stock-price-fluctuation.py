from collections import defaultdict
from heapq import *


# class StockPrice:

#     def __init__(self):
#         self.mx_heap = []
#         self.mn_heap = []
#         self.mp = {}
#         self.latest = -1

#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp > self.latest:
#             self.latest = timestamp
#         self.mp[timestamp] = price
#         heappush(self.mx_heap, (-price, timestamp))
#         heappush(self.mn_heap, (price, timestamp))

#     def current(self) -> int:
#         return self.mp[self.latest]

#     def maximum(self) -> int:
#         price, ts = self.mx_heap[0]
#         price = -price
#         while self.mp[ts] != price:
#             heappop(self.mx_heap)
#             price, ts = self.mx_heap[0]
#         return price

#     def minimum(self) -> int:
#         price, ts = self.mn_heap[0]
#         while self.mp[ts] != price:
#             heappop(self.mn_heap)
#             price, ts = self.mn_heap[0]
#         return price


# # Your StockPrice object will be instantiated and called as such:
# # obj = StockPrice()
# # obj.update(timestamp,price)
# # param_2 = obj.current()
# # param_3 = obj.maximum()
# # param_4 = obj.minimum()


class StockPrice:

    def __init__(self):
        self.current_price = defaultdict()
        self.latest_timestamp = -1
        self.min_hp = []
        self.max_hp = []

    def update(self, timestamp: int, price: int) -> None:
        self.current_price[timestamp] = price
        heappush(self.max_hp, (-price, timestamp))
        heappush(self.min_hp, (price, timestamp))
        if self.latest_timestamp < timestamp:
            self.latest_timestamp = timestamp

    def current(self) -> int:
        return self.current_price[self.latest_timestamp]

    def maximum(self) -> int:
        price, ts = self.max_hp[0]
        price = -price
        while self.max_hp and self.current_price[ts] != price:
            heappop(self.max_hp)
            if self.max_hp:
                price, ts = self.max_hp[0]
                price = -price
        return price


    def minimum(self) -> int:
        price, ts = self.min_hp[0]
        while self.min_hp and self.current_price[ts] != price:
            heappop(self.min_hp)
            if self.min_hp:
                price, ts = self.min_hp[0]
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
