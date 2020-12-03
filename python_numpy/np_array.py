import numpy as np

a1 = np.array([0, 10, 20, 30, 40, 50])
print(a1)
print()

a2 = np.arange(10, 100, 10).reshape(3,3)
print(a2)
print()

a2[0, 2] = 95
print(a2)
print()

b1 = np.array([0, 10, 20, 30, 40, 50])
print(b1[1:4])
print(b1[:3])
print(b1[2:])