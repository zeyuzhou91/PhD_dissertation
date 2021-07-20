"""
The stochastic model of the observation. 
"""

import numpy as np


def norm_pdf(x, mu, var):
    """
    Return the pdf of a normal distribution with mean mu and variance var at value x. 
    """
    
    return 1.0/np.sqrt(2*np.pi*var) * np.exp(-(x-mu)**2/(2*var))


def calculate_likelihood(theta, a, obs, var):
    """
    Calculate the probability of observing obs by playing action a, given 
    that the system parameter is theta. 
    
    Input:
      theta:  a numpy array of shape (N,)
      a:      a numpy array of shape (N,)
      obs:    a real value
      var:    a positive value, the variance of the Gaussian distribution
    """
    
    mu = np.inner(theta, a)
    #lh = st.norm.pdf(obs, mu, scale)
    #lh = norm_pdf(obs, mu, var)
    lh = 1.0/np.sqrt(2*np.pi*var) * np.exp(-(obs-mu)**2/(2*var))
    return lh

