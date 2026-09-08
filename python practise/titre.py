import math
absorbances = [0.4172, 0.4189, 0.4155, 0.4901, 0.4168, 0.4180, 0.4163]

total= sum(absorbances)
n= len(absorbances)
mean=total/n
squares=0
for x in absorbances:
    squares= squares + (x-mean) **2
varience= squares/ (n-1)
sd= math.sqrt(varience)
print("Mean:", round(mean, 4))
print("SD:", round(sd, 4))

