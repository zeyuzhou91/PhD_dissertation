"""
The stochastic model of the observation. 
"""

def calculate_likelihood(theta, a, obs):
    """
    Calculate the probability of observing obs by playing action a, given 
    that the system parameter is theta. 
    
    Input:
      theta:  a vector of values in [0,1], shape(K,)
      a:      a numpy array of integers in [K], shape (M,)
      obs:    0 or 1. 
    """
    
    v = 1-theta[a]  # v is a vector 
    p = 1.0
    for u in v:
        p *= u
    b = 1-p  # the mean/parameter of the combined Bernoulli distribution
    if obs == 1:
        lh = b
    else:
        lh = 1-b
    return lh




