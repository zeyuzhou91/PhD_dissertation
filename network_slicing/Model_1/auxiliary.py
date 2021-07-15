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
    ind = np.argmax(array)
    return ind


def argmax_multi_domain_with_context(G, theta_hat, c):
    """
    Find the best action in the multi-domain network slicing problem, given context c
    and assuming the system parameter is theta_hat. 
    
    Input:
      theta_hat:  a numpy array of dimension (D, max(B), 3).
      c:          the context, a vector of length 3. 
    
    Output:
      a:          an action, a length-D vector of integers
    """
    
    a = np.zeros(G.D, dtype=int)
    for i in range(G.D):
        #print('shape of c: ', np.shape(c))
        #print('theta_hat[i]: ', theta_hat[i][:G.B[i]])
        #print('shape of theta_hat[i]: ', np.shape(theta_hat[i][:G.B[i]]))
        mu = theta_hat[i][:G.B[i]].dot(c)   # the vector of mu's in domain i
        #print('mu =', mu)
        a[i] = int(np.argmax(mu))
        #print('a[i] =', a[i])
    
    return a


def normalize_every_m_values(v, m):
    """
    Given a vector v of non-negative values, normalize it so that every consecutive m values in v
    are a probability vector, i.e. they add up to one.
    
    Input:
       v: an numpy array, a vector of non-negative values
       m: a positve integer
       
    Output:
       u: an numpy array, the normalized version of v
    """
    
    n = len(v)
    k = int(np.ceil(n/m))  # the number of chunks of the vector v
                      # except possibly the last chunk, all chunks have length m
    u = np.zeros(n)
    for i in range(k-1):  # normalize the k-1 chunks
        idx = i*m
        v_chunk = v[idx:(idx+m)]
        u[idx:(idx+m)] = v_chunk / np.sum(v_chunk) 
        
    # normalize the last chunk
    idx = (k-1)*m
    v_chunk = v[idx:]
    u[idx:] = v_chunk / np.sum(v_chunk) 
    
    return u



def map_to_domain(x):
    """
    Map each number in the given array to [0,1]^K, if it is outside of that interval. 
    Further more, for each row vector of the matrix x, every consecutive three values 
    should be a probability distribution. 
    
    Input:
      x:  an numpy array of shape (N,K)
    
    Output:
      y:  an numpy array of shape (N,K)
    """
    
    #print('Before mapping, x=', x)
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
        y = normalize_every_m_values(y, 3)
     
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
            y[i] = normalize_every_m_values(y[i], 3)
    
    #print('After mapping, y=', y)       
    return y