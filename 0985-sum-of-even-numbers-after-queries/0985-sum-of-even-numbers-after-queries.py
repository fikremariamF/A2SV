class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = []
        sum = 0
        for num in nums:
            if num % 2 == 0:
                sum += num
                
        for query in queries:
            prev = nums[query[1]]
            if nums[query[1]] % 2 != 0:
                nums[query[1]] += query[0]
                if nums[query[1]] % 2 == 0:
                    sum += nums[query[1]]
                sums.append(sum)
            else:
                nums[query[1]] += query[0]
                if nums[query[1]] % 2 == 0:
                    sum += query[0]
                    sums.append(sum)
                else:
                    sum -= prev
                    sums.append(sum)
        if sums:
            return sums
        return [0]