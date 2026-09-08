votes = ["red", "red", "blue", "blue", "blue", "red", "red", "red", "red", "green"]

samecolour = 1
samecolour_best = 1
position = 0
bestposition = 0
bestcolour = votes[0]

for v in range(1, len(votes)):

    if votes[v] == votes[v - 1]:
        samecolour = samecolour + 1
    else:
        samecolour = 1
        position = v

    if samecolour > samecolour_best:
        samecolour_best = samecolour
        bestposition = position
        bestcolour = votes[v]

print("Longest run:", samecolour_best)
print("Colour:", bestcolour)
print("Started at position:", bestposition)

