import numpy as np

a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])
m = np.reshape(a,(4,4))
print(m)

#Accessing Element
print("\n Acessomg Elements")
print(a[1])
print(a[2][0])


