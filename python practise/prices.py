price = [120, 135, 130, 180, 175, 240, 236]
best_position=0
biggest_change=0



for p in range(1,len(price)):
    if price[p]> price[p-1]:
        change = price[p] - price[p-1] 

    if change>biggest_change:
                biggest_change=change
                best_position= p 
    
        
print("biggest jump: ", biggest_change)
print("From day ", best_position-1, "to ", best_position)
print("Price went from ", price[best_position -1], "to ", price[best_position])
    
    
        

