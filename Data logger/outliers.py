import numpy as np
print("Data Logger")
results= []
while True:
    user_input= input("results> ") 
    if user_input == "done":        
        break
    if user_input == "":
        continue
    results.append(float(user_input))
a = np.sort(np.array(results))
med = np.median(a)
x=np.abs(a-med)
mad=np.median(x)
mz= 0.6745* (a - med) /mad
bad= np.abs(mz) > 3.5
print("readings:", a)
print("outliers:", a[bad])
print("kept    :", a[~bad])

 

         ##  print("Summary: ")
          # print("Mean: ", np.mean(arr, decimals=2))
           ##print("Standard Deviation: ",np.srd(arr, ddof=0, decimals =2)) 
#for l in list:
               
               #then find sd
