import numpy as np
import bandit
import auxiliary as aux


class System_PTS_a(bandit.System):
    """
    PTS with per-system particles. 
    """
    
    def __init__(self, D, B, T, Npar_sys):
        super().__init__(D, B, T)
        self.Npar = Npar_sys     # number of particles (for the system)
        self.Particles = np.zeros((Npar_sys, D, max(B), 3))   # the set of particles, uninitialized
        self.w = np.ones(Npar_sys) * (1.0/Npar_sys)               # the weights of particles, initialized to be the same


    def init_particles(self):
        """
        Initialize the set of particles. 
        """
        
        # Method 1: Each particle is a dimension-(D, max(B), 3) numpy array. 
        # We generate each particle by generating a length-3 probability vector
        # uniformaly at random for each entry of that particle
        for k in range(self.Npar):
            for i in range(self.D):
                for j in range(self.B[i]):
                    p = np.random.uniform(0, 1, 3)  # a length-3 vector
                    self.Particles[k][i][j] = p/sum(p)   # normalize p to be a probability vector
        #print('Particles =', self.Particles)              
        return None 
    
    
    def select_action(self, t, c):
        """
        Select the best action under the context c. 
          
        Input:
          t:    the round index, 0 <= t <= T-1.
          c:    the context, a numpy array in [0,1]^3 
          
        Output:
          a:   an action/arm, a integer vector of length D.
        """
        
        theta_hat = self.generate_parameter_sample()
        #print('theta_hat:', theta_hat)
        
        a = aux.argmax_multi_domain_with_context(self, theta_hat, c)
        #print('Actual Action:', a)        
        return a     
    

    def generate_parameter_sample(self):
        """
        Generate a sample theta_hat (one particle) based on the current weights on the particles. 
                
        Output:
          theta_hat: a numpy array of dimension (D, max(B), 3).
        """   
        
        theta_hat = np.zeros((self.D, max(self.B), 3)) 
        k = np.random.choice(self.Npar, 1, p=self.w)[0]  # np.random.choice outputs an array
        theta_hat = self.Particles[k]   
        return theta_hat


    def update_state(self, c, a, obs, t):
        """
        Update the state variables, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^3 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector. 
          t:    the round index, 0 <= t <= T-1. 
        """
        
        self.update_weights(c, a, obs, t)   # only update weights, not particles   
        return None 


    def update_weights(self, c, a, obs, t):
        """
        Update the weights of the particles, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^3 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector.  
          t:    the round index, 0 <= t <= T-1.
        """
        
        new_w = np.zeros(self.Npar)  # the unnormalized new weight vector
        for k in range(self.Npar):
            lh = self.calculate_likelihood(self.Particles[k], c, a, obs)
            #print('likelihood =', lh)
            new_w[k] = lh * self.w[k]
        new_w = 1.0/(np.sum(new_w)) * new_w   # normalizing
        #print('new_w =', new_w)
        self.w = new_w
        return None 


    def calculate_likelihood(self, theta, c, a, obs):
        """
        Calculate the probability of observing obs by playing action a under context c,
        given that the system parameter is theta. 
        
        Input:
          theta:  system parameter, a numpy array of dimension (D, max(B), 3)
          c:      the context, a numpy array in [0,1]^3
          a:      the action, a length-D vector of integers 
          obs:    the observation, a binary length-D vector 
        """
                
        lh = 1.0
        for i in range(self.D):
            p = theta[i][a[i]].dot(c)  # the parameter p of a Bernoulli distribution
            if obs[i] == 1:
                lh = lh * p
            else:
                lh = lh * (1-p)
        return lh
    
    
class System_PTS_b(bandit.System):
    """
    PTS with per-block particles. 
    """    
    
    def __init__(self, D, B, T, Npar_blk):
        super().__init__(D, B, T)
        self.Npar = Npar_blk     # number of particles (for each resource block)
        self.Particles = np.zeros((D, max(B), Npar_blk, 3))   # the set of particles, uninitialized
        self.w = np.ones((D, max(B), Npar_blk)) * (1.0/Npar_blk)  # the weights of particles, initialized to be the same


    def init_particles(self):
        """
        Initialize the set of particles. 
        """
        
        # Method 1: The set of resource blocks is a numpy array of dimension (D, max(B)).
        # Each resource block has Npar particles, where each particle is a length-3 probability vector.
        # We generate each particle for each block by generating a length-3 probability vector
        # uniformaly at random.
        for i in range(self.D):
            for j in range(self.B[i]):
                for k in range(self.Npar):
                    p = np.random.uniform(0,1,3)  # a length-3 vector
                    #print('self.Particles[i][j][k] =', self.Particles[i][j][k])
                    self.Particles[i][j][k] = p/sum(p) # normalize p to be a probability vector        
        #print('Particles =', self.Particles)        
        return None 
    
    
    def select_action(self, t, c):
        """
        Select the best action under the context c. 
          
        Input:
          t:    the round index, 0 <= t <= T-1.
          c:    the context, a numpy array in [0,1]^3 
          
        Output:
          a:   an action/arm, a integer vector of length D.
        """
        
        theta_hat = self.generate_parameter_sample()
        #print('theta_hat:', theta_hat)
        
        a = aux.argmax_multi_domain_with_context(self, theta_hat, c)
        #print('Actual Action:', a)        
        return a     
    

    def generate_parameter_sample(self):
        """
        Generate a sample theta_hat (one particle) based on the current weights on the particles. 
                
        Output:
          theta_hat: a numpy array of dimension (D, max(B), 3).
        """   
                
        theta_hat = np.zeros((self.D, max(self.B), 3)) 
        for i in range(self.D):
            for j in range(self.B[i]):
                k = np.random.choice(self.Npar, 1, p=self.w[i][j])[0]  # np.random.choice outputs an array
                theta_hat[i][j] = self.Particles[i][j][k]   
        # ZEYU: is there a quicker way to implement this?        
        return theta_hat


    def update_state(self, c, a, obs, t):
        """
        Update the state variables, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^3 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector. 
          t:    the round index, 0 <= t <= T-1. 
        """
        
        self.update_weights(c, a, obs, t)   # only update weights, not particles   
        return None 


    def update_weights(self, c, a, obs, t):
        """
        Update the weights of the particles, given context c, action a and observation obs.
        The updating rule is essentially a discretized Bayesian update. 
        
        Input:
          c:    the context, a numpy array in [0,1]^3 
          a:    an action/arm, a integer vector of length D. 
          obs:  the observation, a binary length-D vector.
          t:    the round index, 0 <= t <= T-1.
        """        
        
        for i in range(self.D):  # in each domain, we only update the particles' weights for the block used, while the particles' weights for other blocks remain unchanged
            new_w = np.zeros(self.Npar)  # the unnormalized new weight vector
            for k in range(self.Npar):
                lh = self.calculate_likelihood_for_block(self.Particles[i][a[i]][k], c, obs[i])
                #print('likelihood =', lh)
                new_w[k] = lh * self.w[i][a[i]][k]
            new_w = 1.0/(np.sum(new_w)) * new_w   # normalizing
            #print('new_w =', new_w)
            self.w[i][a[i]] = new_w        
        
        return None 


    def calculate_likelihood_for_block(self, v, c, obs):
        """
        Calculate the probability of observing obs produced by a resource block by playing action a under context c,
        given that the block parameter is v. 
        
        Input:
          v:      block parameter, a length-3 probability vector, a numpy array
          c:      the context, a numpy array in [0,1]^3
          obs:    the observation, 0 or 1 
          
        Output:
          lh:     a number in [0,1], the likelihood/probability.   
        """
        
        mu = v.dot(c)
        if obs == 1:
            lh = mu
        else:
            lh = 1-mu        
        return lh