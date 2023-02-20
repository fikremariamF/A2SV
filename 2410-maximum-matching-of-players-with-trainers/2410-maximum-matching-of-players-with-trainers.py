class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        groups = [[] for _ in trainers]
        counter = 0
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(players):
            if ptr2 == len(trainers):
                ptr2 = 0
            if players[ptr1] <= trainers[ptr2]:
                groups[ptr2].append(players[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif players[ptr1] > trainers[ptr2]:
                ptr2 += 1
            if ptr1 < len(players) and players[ptr1] > trainers[-1]:
                break
        for group in groups:
            if group:
                counter += 1
        return counter