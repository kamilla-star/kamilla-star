import numpy as np

a = np.array([0.4172, 0.4189, 0.4155, 0.4901, 0.4168, 0.4180, 0.4163])

print("Sum:     ", a.sum())
print("n:       ", len(a))
print("Mean:    ", round(a.mean(), 4))
print("Variance:", a.var(ddof=1))
print("SD:      ", round(a.std(ddof=1), 4))
print("Min/Max: ", a.min(), a.max())