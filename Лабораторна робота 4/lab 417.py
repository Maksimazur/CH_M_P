import numpy as np
a = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5') #Завдання 1
c = np.linalg.matrix_rank(a)
print(c)