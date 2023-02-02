class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, j = 0, len(people) - 1
        counter = 0
        people.sort()
        while i <= j:
            counter += 1
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
        return counter