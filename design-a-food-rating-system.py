from typing import List
from heapq import *
from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heaps = []
        self.cuisine_to_index_mapping = {}
        self.latest = dict()
        self.mx = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            cuisine_index = None
            if cuisine in self.cuisine_to_index_mapping:
                cuisine_index = self.cuisine_to_index_mapping[cuisine]
            else:
                cuisine_index = len(self.heaps)
                self.cuisine_to_index_mapping[cuisine] = cuisine_index
                self.heaps.append([])
            self.latest[food] = rating
            self.mx[cuisine] = max(self.mx.get(cuisine, -1), rating)
            heappush(self.heaps[cuisine_index], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.latest[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[self.cuisine_to_index_mapping[cuisine]]
        rating, food = heap[0]
        rating = -rating
        while heap and self.latest[food] != rating:
            heappop(heap)
            if heap:
                rating, food = heap[0]
                rating = -rating
        return food


# Your FoodRatings object will be instantiated and called as such:
foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
ratings = [9,12,8,15,14,7]
obj = FoodRatings(foods, cuisines, ratings)
param_2 = obj.highestRated("korean")
param_2 = obj.highestRated("japanese")
obj.changeRating("sushi",16)
param_2 = obj.highestRated("japanese")
obj.changeRating("ramen",16)
param_2 = obj.highestRated("japanese")
