temps= [ 18,22,25,19,21,23,24,17,26]
warm_day=0
streak=0
best_streak=0
current_start=0
best_start=0

for t in range(len(temps)):
    if temps[t] > 20:
         warm_day = warm_day + 1
         if streak == 0:
             current_start=t
         streak = streak + 1
         if streak > best_streak:
             best_streak = streak
             best_start=current_start
    else:
        streak=0
print ("total amount of warm days: ", warm_day)
print ("The longest warm spell: ", best_streak)
print ("Spell started on day: ", best_start)