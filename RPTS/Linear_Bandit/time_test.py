import time
import scipy.stats as st
import numpy as np


def f(x, mu, var):
    return 1.0/np.sqrt(2*np.pi*var) * np.exp(-(x-mu)**2/(2*var))
    

start = time.time()
for i in range(100*1000):
    x = st.norm.pdf(0, 0, 1)
print('Duration = %.3f' % (time.time()-start))


start = time.time()
for i in range(100*1000):
    x = f(0, 0, 1)
print('Duration = %.3f' % (time.time()-start))

print(st.norm.pdf(10,10,10))
print(f(10,10,100))