"""
The stochastic model of the observation. 
"""

def calculate_likelihood(theta, a, obs):
    """
    Calculate the likelihood/probability of observing obs, if the parameter is theta. 
    
    Input:
      theta:  a vector of values in [0,1], shape(K,)
      a:      an integer in [K] = {0, 1, ..., K-1}
      obs:    0 or 1. 
    
    Output:
      lh:     a number in [0,1], the likelihood/probability. 
    """
    
    if obs == 1:
        lh = theta[a]
    else:
        lh = 1-theta[a]
    
    return lh