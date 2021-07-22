"""
In this module, the particle Thompson sampling algorithm is implemented as a 
sub-class of the game.System class. 
"""

import numpy as np
import game
import auxiliary as aux
import model


class System_PTS(game.System): 
    def __init__(self, K, T, Npar):
        super().__init__(K, T) 
        self.Npar = Npar                        # number of particles
        self.Particles = np.zeros(Npar)         # the set of particles, un-initialized
        self.w = np.ones(Npar) * (1.0/Npar)     # the weights of the particles, initialized to be all having equal weights
        self.w_bar = np.ones(Npar) * (1.0/Npar) # the running average weights of the particles 
    
    def init_particles(self):
        """
        Initialize the set of particles. 
        """
        
        # Each particle is a dimension-K vector. We generate each particle 
        # uniformly at random from the space [0,1]^K. 
        self.Particles = np.random.uniform(0, 1, (self.Npar, self.K))
        #print("Particles: ", self.Particles) 
        return None    
    
    
    def select_action(self, t):
        """
        Use Particle Thompson Sampling to select an action.
          
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:   an action/arm, an integer in [K]. 
        """
        
        theta_hat = self.generate_parameter_sample(t)
        #print('theta_hat:', theta_hat)
        
        a = aux.argmax_of_array(theta_hat)
        #print('Actual Action:', a)
        
        return a 
    
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. 
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles   
        self.update_running_average_weights(t) 
        return None    


    def update_weights(self, a, obs, t):
        """
        Update the weights of the particles.  
        
        Input:
          a:    the action/arm taken in round t, an integer. 
          obs:  the observation incurred in round t, 0 or 1.
          t:    the round index, 0 <= t <= T-1. 
        """
        
        new_w_tilde = np.zeros(self.Npar)  # the unnormalized new weight vector
        for k in range(self.Npar):
            lh = model.calculate_likelihood(self.Particles[k], a, obs)
            #print('likelihood =', lh)
            new_w_tilde[k] = lh * self.w[k]
        new_w = 1.0/(np.sum(new_w_tilde)) * new_w_tilde   # normalizing
        #print('new_w =', new_w)
        self.w = new_w
    
        return None    
    
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        
        Input:
          t:    the round index, 0 <= t <= T-1. 
        """    
        
        self.w_bar = self.w_bar * (float(t)/(t+1)) + self.w / float(t+1) 
        #print('Running average particle weigths =', self.w_bar)
        return None    
    

    def generate_parameter_sample(self, t):
        """
        Generate a sample theta_hat (one particle) based on the current weights on the particles. 
        
        Input:
          t:    the round index, 0 <= t <= T-1.
        
        Output:
          theta_hat: a length-K vector of values in [0,1].
        """   
        
        theta_hat = np.zeros(self.K) 
        k = np.random.choice(self.Npar, 1, p=self.w)[0]  # np.random.choice outputs an array
        theta_hat = self.Particles[k]      
        return theta_hat
