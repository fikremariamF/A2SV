class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        data = {}
        for winner, losser in matches:
            if winner in data:
                data[winner][0] += 1
                data[winner][1] += 1
            else:
                data[winner] = [1,1,0]
            if losser in data:
                data[losser][0] += 1
                data[losser][2] += 1
            else:
                data[losser] = [1,0, 1]
        # print(data)
        zero_losses = []
        one_loss = []
        for player in data:
            losses = data[player][0] - data[player][1]
            if data[player][2] == 0:
                zero_losses.append(player)
            elif data[player][2] == 1:
                one_loss.append(player)
        zero_losses.sort()
        one_loss.sort()
        return zero_losses, one_loss
        