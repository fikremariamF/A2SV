class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mydict = {}
        count = 0
        for value in points:
            if value[0] == x or value[1] == y:
                # print(mydict.values())
                if (value[0],value[1]) not in mydict.keys():
                    # print("in here")
                    mydict[(value[0],value[1])] = [count,"v"]   
            else:
                mydict[(value[0],value[1])] = [count, "n"]
            count += 1
        points.sort(key= lambda m: abs(x - m[0]) + abs(y - m[1]))
        # print(mydict.values())
        # print(points, mydict)
        # print(mydict)
        for value in points:
            if mydict[(value[0],value[1])][1] == "v":
                # print(value)
                # print(mydict[(value[0],value[1])])
                return mydict[(value[0],value[1])][0]
        
        return -1