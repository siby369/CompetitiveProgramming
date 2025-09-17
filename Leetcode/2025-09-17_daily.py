"""
Problem: 2353. Design a Food Rating System
Difficulty: Medium
Link: https://leetcode.com/problems/design-a-food-rating-system/

Approach:
- Use two main data structures:
  1. A dictionary `mp` mapping food -> (cuisine, rating).
  2. A dictionary `data` mapping cuisine -> SortedList of (-rating, food).
     - Negative rating ensures highest rating comes first (SortedList is ascending).
     - Food name breaks ties lexicographically.
- For initialization:
  - Store (cuisine, rating) in `mp`.
  - Insert (-rating, food) into the corresponding cuisine's SortedList.
- For `changeRating(food, newRating)`:
  - Lookup current cuisine and rating from `mp`.
  - Remove old (-rating, food) from SortedList and insert (-newRating, food).
  - Update `mp`.
- For `highestRated(cuisine)`:
  - Return the food at index 0 of the SortedList, which is the highest-rated one.

Time Complexity:
- Initialization: O(n log n), since each insert into SortedList is O(log n).
- changeRating: O(log n), remove + add in SortedList.
- highestRated: O(1), direct access to first element.
Space Complexity: O(n), to store all mappings and SortedLists.
"""


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp={}
        self.data=defaultdict(SortedList)
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.mp[food]=(cuisine,rating)
            self.data[cuisine].add((-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine,rating=self.mp[food]
        self.mp[food]=(cuisine,newRating)
        self.data[cuisine].remove((-rating,food))
        self.data[cuisine].add((-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]

