"""
Problem: Design Movie Rental System
Difficulty: Hard
Link: https://leetcode.com/problems/design-movie-rental-system/

Approach:
- The system needs to support efficient operations for searching, renting, dropping, and reporting movies.
- Data Structures:
  - `available`: Dictionary mapping each movie → `SortedSet` of (price, shop) where the movie is currently available.
  - `rented`: `SortedSet` of (price, shop, movie) for currently rented movies, kept globally.
  - `priceMap`: Dictionary mapping (shop, movie) → price for quick lookups.
- Methods:
  - `search(movie)`:
    - Return up to 5 shops (lowest price, then smallest shop ID) where the movie is available.
  - `rent(shop, movie)`:
    - Remove (price, shop) from `available[movie]` and add (price, shop, movie) to `rented`.
  - `drop(shop, movie)`:
    - Remove (price, shop, movie) from `rented` and restore (price, shop) to `available[movie]`.
  - `report()`:
    - Return up to 5 rented movies as `[shop, movie]`, sorted by price, shop ID, and movie ID.
- Using `SortedSet` ensures efficient insertion, removal, and ordered iteration.

Time Complexity:
- `search`: O(1) to O(log n), limited to 5 extractions.
- `rent` / `drop`: O(log n), for updates in `SortedSet`.
- `report`: O(1) to O(log n), limited to 5 outputs.

Space Complexity: O(m), where m = total number of movie entries.
"""


class MovieRentingSystem:
    def __init__(self,n: int,entries: list[list[int]]):
        from sortedcontainers import SortedSet
        self.available={}
        self.rented=SortedSet()
        self.priceMap={}
        for shop,movie,price in entries:
            if movie not in self.available:
                self.available[movie]=SortedSet()
            self.available[movie].add((price,shop))
            self.priceMap[(shop,movie)]=price

    def search(self,movie: int) -> list[int]:
        res=[]
        if movie in self.available:
            for price,shop in self.available[movie]:
                res.append(shop)
                if len(res)==5: 
                    break
        return res

    def rent(self,shop: int,movie: int) -> None:
        price=self.priceMap[(shop,movie)]
        self.available[movie].remove((price,shop))
        self.rented.add((price,shop,movie))

    def drop(self,shop: int,movie: int) -> None:
        price=self.priceMap[(shop,movie)]
        self.rented.discard((price,shop,movie))
        self.available[movie].add((price,shop))

    def report(self) -> list[list[int]]:
        res=[]
        for price,shop,movie in self.rented:
            res.append([shop,movie])
            if len(res)==5: 
                break
        return res
