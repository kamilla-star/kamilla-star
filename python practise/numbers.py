tickets = [3, 4, 5, 9, 10, 20, 21, 22, 23, 40]
position=0
best_position=0
streak=1
best_streak=1
for t in range(1, len(tickets)):
    if tickets[t] == tickets[t-1]+1:
        streak=streak+1
    else:
        streak=1
        position=t
    if streak> best_streak:
        best_streak=streak
        best_position=position 

print("longest run: ", best_streak)
print("best run started at position: ", best_position)  
print("best run started at number: ", tickets[best_position])
    
