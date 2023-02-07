class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0 , 0
        fruit_type = {}
        max_len = 0
        while r < len(fruits):
            fruit_type[fruits[r]] = r
            if len(fruit_type) >= 3:
                min_val = min(fruit_type.values())
                del fruit_type[fruits[min_val]]
                l = min_val + 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
                
                