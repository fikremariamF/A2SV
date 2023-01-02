from collections import Counter

iterations = int(input())

costs = []
for iteration in range(iterations):
    first_input = list(map(int,input().split()))
    orbits = input().split()

    planets_in_orbit = Counter(orbits)
    # print(planets_in_orbit)
    orbits_set = set(orbits)
    # print(orbits_set)
    cost = 0
    for orbit in orbits_set:
        # print("for all in orbit:", first_input[1])
        if first_input[1] > planets_in_orbit[orbit]:
            # print("in first")
            cost += planets_in_orbit[orbit]
        else:
            # print("in second")
            cost += first_input[1]
    costs.append(cost)

for cost in costs:
    print(cost)
