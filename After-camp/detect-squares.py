class DetectSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total_squares = 0
        points_list = list(self.points_count.keys())

        for (px, py) in points_list:
            # Same logic as before
            count = self.points_count[(px, py)]
            if px == x or py == y:
                continue

            if abs(px - x) == abs(py - y):
                total_squares += (
                    self.points_count.get((x, py), 0) *
                    self.points_count.get((px, y), 0) *
                    count
                )

        return total_squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)