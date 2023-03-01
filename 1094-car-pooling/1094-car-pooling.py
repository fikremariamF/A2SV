class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = max(trips, key= lambda x: x[2])[2]
        distance = [0] * (length+3)
        for trip in trips:
            distance[trip[1]] += trip[0]
            distance[trip[2]] -= trip[0]
        for idx in range(length + 3):
            distance[idx] += distance[idx-1]
        # print(distance)
        if max(distance) > capacity:
            return False
        return True