import time
import numpy as np
import random

N = 1000000

p1 = time.time()
for i in range(N):
    np.random.uniform(0,1,1)
print('Duration using np.random.uniform = %.3f' % (time.time()-p1))


p2 = time.time()
for i in range(N):
    random.uniform(0,1)
print('Duration using random.uniform = %.3f' % (time.time()-p2))