results = ["win", "win", "loss", "win", "win", "win", "loss", "win", "win"]
total_wins = 0
current = 0
best = 0
current_start = 0
best_start = 0

for i in range(len(results)):
    if results[i] == "win":
        total_wins = total_wins + 1
        if current == 0:
            current_start = i
        current = current + 1
        if current > best:
            best = current
            best_start = current_start
    else:
        current = 0

print("Total wins: ", total_wins)
print("Longest streak: ", best)
print("Streak started at position: ", best_start)