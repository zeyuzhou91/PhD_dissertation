"""
In this module, the regenerative particle Thompson sampling (RPTS) algorithms, 
including RPTS-1 and RPTS-2, are implemented as a sub-class of the PTS.System_PTS class. 
"""

import numpy as np
import PTS
import auxiliary as aux
import random


class System_RPTS1(PTS.System_PTS): 
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.w_inact = 0.001           # if f_del fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.f_del = 0.8               # delete this fraction of particles at each regeneration
        self.w_new = 0.01              # the aggregate weight assigned to the newly re-generated particles
        
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action, a numpy array of integers in [K] of shape (M,)
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.f_del), self.w_inact):
            self.kill_and_regenerate_particles(t)
            
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.f_del)   # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        Sigma = cov
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, Sigma) # particles killed and regenerated
        self.w = reweight(self, self.w, die, idx)
        return None


class System_RPTS2(PTS.System_PTS): 
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.w_inact = 0.001           # if f_del fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.f_del = 0.8               # delete this fraction of particles at each regeneration
        self.w_new = 0.01              # the aggregate weight assigned to the newly re-generated particles  
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action, a numpy array of integers in [K] of shape (M,)
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.f_del), self.w_inact):
            self.kill_and_regenerate_particles(t)
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.f_del)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        Sigma = np.trace(cov) / self.K * np.eye(self.K) 
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, Sigma) # particles killed and regenerated
        self.w = reweight(self, self.w, die, idx)
        return None



def is_paralyzed(v, num, threshold):
    """
    Decide if the num lowest valued entries in vector v add up to less than threshold. 
    
    Input:
       v:     a weight vector, a numpy array. 
       num:   an integer. 
       threshold:  a decimal number in [0,1], typically small. 
       
    Output:
      True or False.
    """

    w = np.copy(v)    # make a copy of v without reference
    w.sort()          # sort w from smallest value to largest value
    val = sum(w[:num])
    if val < threshold:
        return True
    else:
        return False    
    

def guided_Gaussian_exploration(G, n, mu, Sigma):
    """
    Generate n particles according to Gaussian(mu, Sigma).
    
    Inputs:
      G: the game instance.
      n: an integer, generate this number of particles. 
      mu:  the mean of the Gaussian distribution.
      Sigma:  the covariance matrix of the Gaussian distribution. 
    
    Output:
      Par: an numpy array of dimension (n, G.K), where each row is a particle. 
    """
    
    Par = aux.map_to_domain(np.random.multivariate_normal(mu, Sigma, n))
    return Par


def reweight(G, w, n, idx):
    """
    Re-set the particle weight vector. Give the entries at idx[:n] a total weight of G.w_new. 
    Scale other entries so that all entries still add up to one.
    
    Inputs:
      w:  a numpy array, the weight vector before update
      n:  an integer, the weights of this number of entries need to be reset. 
      idx: a numpy array of integers, the index array.
      
    Output:
      v:  a numpy array, the updated weight vector. 
    """
        
    v = np.copy(w)
    v[idx[:n]] = np.ones(n) * (G.w_new/n)               # weights of the re-generated particles: total weight = w_new
    v[idx[n:]] *= (1-G.w_new) / (sum(v[idx[n:]]))       # weights of the survived particles: total weight = 1-w_new 
    return v
    
    
def calculate_empirical_stats(w, X):
    """
    Calculate the empirical mean and covariance matrix of the data in X with respect to weights w. 
    
    Inputs:
      w: a numpy array, a weight vector of shape (N,).
      X: a numpy array, shape (N,K)
      
    Outputs:
      mu: a numpy array of shape (K,)
      cov: a numpy array of shape (K,K) 
      
    Example:
    w = [w1 w2 w3 w4 w5]   N=5
    X = [x1   x2]
      = [x11  x21
         x12  x22
         x13  x23
         x14  x24
         x15  x25]
    K=2
    
    mu = [E[x1] E[x2]] is the weighted average of the 5 row vectors
    cov = [E[x1^2]  E[x1*x2]
           E[x2*x1] E[x2^2]]
    where all the expectations are with respect to the weight w. 
    
    Example:
    w = [0.2 0.3 0.5]
    X = [1 2
         3 1
         4 4]
    
    then
    mu = [3.1 2.7]
    cov = [1.29 0.93
           0.93 1.81]
    """
    
    (N,) = np.shape(w)
    #print('N =', N)
    #print('np.shape(w) =', np.shape(w))
    
    mu = w.dot(X)
    #print('mu =', mu)
    #print('np.shape(mu) =', np.shape(mu))

    Y = X-mu    # Y is the shifted version of X with mean zero
    #print('Y =', Y)
    
    v = np.sqrt(w)  # the element-wise square-root of w
    v = v.reshape(N,1)  # reshape into a column vector
    #print('v =', v)
    
    Z = v*Y         # element-wise scaling of each column of Y
    cov = Z.T.dot(Z)
    #print('cov =', cov)
    #print('np.shape(cov) =', np.shape(cov))
    return (mu, cov)

    
    
    