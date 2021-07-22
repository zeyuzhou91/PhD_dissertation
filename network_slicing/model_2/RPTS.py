import numpy as np
import PTS
import auxiliary as aux


class System_RPTS2_a(PTS.System_PTS_a):
    """
    RPTS2 with per-system particles. 
    """
    
    def __init__(self, D, B, T, Npar):
        super().__init__(D, B, T, Npar) 
        self.w_inact = 0.001           # if f_del fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.f_del = 0.8               # delete this fraction of particles at each regeneration
        self.w_new = 0.01              # the aggregate weight assigned to the newly re-generated particles
        
    
    def update_state(self, c, a, obs, t):
        """
        Update the state variables, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^2 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector. 
          t:    the round index, 0 <= t <= T-1. 
        """
        
        self.update_weights(c, a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.f_del), self.w_inact):
            self.kill_and_regenerate_particles(t)
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        #print('t =', t)
        die = int(self.Npar * self.f_del)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        Par = reshape_particles_tensor_to_vector(self, self.Particles)
        
        (mu, cov) = calculate_empirical_stats(self.w, Par)
        #print('mu =', mu)
        #print('cov =', cov)
        K = sum(self.B) * 2
        Sigma = np.trace(cov) / K * np.eye(K)
        #print('Sigma =', np.diag(Sigma))  
        
        Par_new = guided_Gaussian_exploration(self, die, mu, Sigma) # particles killed and regenerated
        
        self.Particles[idx[:die]] = reshape_particles_vector_to_tensor(self, Par_new)
        self.w = reweight(self, self.w, die, idx)
        return None
   


class System_RPTS2_b(PTS.System_PTS_b):
    """
    RPTS2 with per-block particles. 
    """
    
    def __init__(self, D, B, T, Npar):
        super().__init__(D, B, T, Npar) 
        self.w_inact = 0.001           # if f_del fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.f_del = 0.8               # delete this fraction of particles at each regeneration
        self.w_new = 0.01              # the aggregate weight assigned to the newly re-generated particles
        
    
    def update_state(self, c, a, obs, t):
        """
        Update the state variables, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^2 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector. 
          t:    the round index, 0 <= t <= T-1. 
        """
        
        self.update_weights(c, a, obs, t)   # only update weights, not particles 
        
        for i in range(self.D):  # check the one block used in each domain
            if is_paralyzed(self.w[i][a[i]], int(self.Npar*self.f_del), self.w_inact):
                self.kill_and_regenerate_particles(i, a[i], t)
        return None
    

    def kill_and_regenerate_particles(self, i, j, t):
        """
        Kill and regenerate the particles in Domain i, Block j. 
        """    
        
        die = int(self.Npar * self.f_del)  # kill this number of particles
        idx = np.argpartition(self.w[i][j], die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w[i][j], self.Particles[i][j])
        #print('mu =', mu)
        #print('cov =', cov)
        K = 2  # the parameter for each block is a 2-dimensional (probability) vector
        Sigma = np.trace(cov) / K * np.eye(K)
        #print('Sigma =', Sigma)  
        
        Par_new = guided_Gaussian_exploration(self, die, mu, Sigma) # particles killed and regenerated
        
        self.Particles[i][j][idx[:die]] = Par_new
        self.w[i][j] = reweight(self, self.w[i][j], die, idx)
        return None




def reshape_particles_tensor_to_vector(G, P_tensor):
    """
    Reshape the particles. Flatten each particle from a tensor to a vector. 
    
    Input:
       P_tensor:  an np.array of dimension (Npar, D, max(B), 2). Note that Npar here is the number of per-system particles. 
       
    Output:
       P_vector:  an np.array of dimension (Npar, sum(B)*2).
    """
    
    #print('np.shape(P_tensor) =', np.shape(P_tensor))
    P_vector = P_tensor.reshape((G.Npar, int(sum(G.B)*2)))
    #print('np.shape(P_vector) =', np.shape(P_vector))
    
    return P_vector


def reshape_particles_vector_to_tensor(G, P_vector):
    """
    Reshape the particles. Re-stack each particle from a vector to a tensor. 
    
    Iutput:
       P_vector:  an np.array of dimension (N_new, sum(B)*2).
    
    Output:
       P_tensor:  an np.array of dimension (N_new, D, max(B), 2). Note that Npar here is the number of per-system particles. 
    """
    
    #print('np.shape(P_vector) =', np.shape(P_vector))
    (N_new,b) = np.shape(P_vector)
    P_tensor = P_vector.reshape((N_new, G.D, max(G.B), 2))
    #print('np.shape(P_tensor) =', np.shape(P_tensor))
    
    return P_tensor
    

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
      Par: an numpy array of dimension (n, K), where each row is a particle. 
    """
    
    Par = aux.map_to_domain(np.random.multivariate_normal(mu, Sigma, n))
    return Par


def reweight(G, w, n, idx):
    """
    Re-set the particle weight vector. Give the entries at idx[:n] a total weight of G.rebirth_weight. 
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


#w = np.array([0.2, 0.3, 0.5])
#X = np.array([[1,2], [3,1], [4,4]])
#calculate_empirical_stats(w, X)



    
    
    