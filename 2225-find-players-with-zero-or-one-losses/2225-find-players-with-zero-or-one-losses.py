class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}
        for match in matches:
            wins[match[0]] = wins.get(match[0],0) + 1
            losses[match[1]] = losses.get(match[1],0) + 1
        winners = []
        lossers = []
        for player in losses:
            if losses[player] == 1:
                lossers.append(player)
        for player in wins:
            if player not in losses.keys():
                winners.append(player)
        winners.sort()
        lossers.sort()
        return [winners,lossers]