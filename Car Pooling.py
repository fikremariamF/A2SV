class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda value: value[2])
        maxnum = trips[-1][-1]
        trips.sort(key=lambda value: value[1])
        list = [0] * maxnum
        # mylist = []
        for i in range(0,len(trips)):
            for j in range(trips[i][1],trips[i][2]):
                list[j] += trips[i][0]
            # print(list)
            
        if max(list) > capacity:
            return False
        return True
