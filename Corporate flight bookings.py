class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0]* n
        events = []
        # newout = [0] * n
        for booking in bookings:
            events.append([booking[0]-1,booking[2]])
            events.append([booking[1],-booking[2]])
        # print(events)
        events.sort(key= lambda x: x[0])
        # print(events)
        for event in events:
            if event[0] < n:
                output[event[0]] += event[1]
        for i in range(1, len(output)):
            output[i] = output[i] + output[i-1]
        return output
