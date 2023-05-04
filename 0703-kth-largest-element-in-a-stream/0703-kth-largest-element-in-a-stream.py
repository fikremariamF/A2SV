class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(nums)
        

    def add(self, val: int) -> int:
        
        if len(self.nums) >= self.k:
            heappushpop(self.nums, val)
        else:
            heappush(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)