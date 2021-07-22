"""
Some auxiliary functions.
"""


import numpy as np



def generate_uniform_points_in_ball(r, N, D):
    """
    Generate N points uniformly at random in the radius-r ball in R^D.
    
    Inputs:
      r:   a positive value, the radius of the ball
      N:   a positive integer, the number of points to be generated
      D:   a positive integer, the dimension of the space
      
    Output:
      X:   a numpy array. If N=1, shape is (D,); if N>1, shape is (N,D), each row is a point. 
    """
    
    X = np.random.multivariate_normal(np.zeros(D), np.eye(D), N)
    #print('X =', X)
    for i in range(N):
        x = X[i,:]
        U = np.random.uniform(0,1,1)
        #print('U =', U)
        X[i,:] = (x/np.linalg.norm(x)) * U**(1.0/D) * r
        #print('X =', X)
        
    if N == 1:
        X = X.reshape(D,)
    return X


def argmin_of_array(array, num):
    """
    Return the indices of the the lowest num values in the array. 
    
    Inputs:
      array:   a numpy array. 
      num: an integer.
    
    Output:
      idx:  a numpy array of integer indices.
    """
    
    idx = np.argpartition(array, num)  
    return idx




    

    
    