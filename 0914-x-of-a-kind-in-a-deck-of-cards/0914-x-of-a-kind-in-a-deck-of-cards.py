class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        groups = Counter(deck)
        length_of_group = None
        for key, value in groups.items():
            if length_of_group == None:
                length_of_group = value
            else:
                if length_of_group != value:
                    minimum = math.gcd(value, length_of_group)
                    if minimum == 1:
                        return False
                    length_of_group = minimum
        return True