"""
Some auxiliary functions.
"""

import numpy as np
import scipy as sp
import scipy.stats as st



def argmax_of_array(array):
    """
    Find the index of the largest value in an array of real numbers. 
    
    Input:
      array:  an array of real numbers. 
    
    Output:
      index:  an integer in [K], where K = len(array)
    """

    # Simple but does not support random selection in the case of more than one largest values. 
    ind = int(np.argmax(array))
    
    return ind



def argmin_of_array(array, num):
    """
    Return the indices of the the lowest num values in the array. 
    
    Inputs:
      array:   a numpy array. 
      num:     an integer.
    
    Output:
      idx:  a numpy array of integer indices.
    """
    
    idx = np.argpartition(array, num)  
    return idx


def map_to_domain(x):
    """
    Map each number in the given array to [0,1]^K, if it is outside of that interval. 
    
    Input:
      x:  an numpy array of shape (N,K)
    
    Output:
      y:  an numpy array of shape (N,K)
    """
    y = np.copy(x)
    
    if np.ndim(x) == 1:
        (N,) = np.shape(x)
        for i in range(N):
            if y[i] < 0:
                y[i] = 0
            elif y[i] > 1:
                y[i] = 1
            else:
                pass
     
    elif np.ndim(x) == 2:
        (N,K) = np.shape(x)
        for i in range(N):
            for j in range(K):
                if y[i][j] < 0:
                    y[i][j] = 0
                elif y[i][j] > 1:
                    y[i][j] = 1
                else:
                    pass
    
    return y
