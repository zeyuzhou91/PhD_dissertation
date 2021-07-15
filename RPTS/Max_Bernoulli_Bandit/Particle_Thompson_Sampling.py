import numpy as np
import scipy as sp
import scipy.stats as st
import Game
import auxiliary as aux
import model


class System_PTS(Game.System): 
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T) 
        self.Npar = Npar                        # number of particles
        self.Particles = np.zeros(Npar)    # the set of particles, un-initialized
        self.w = np.ones(Npar) * (1.0/Npar)     # the weights of the particles, initialized to be all having equal weights
        self.w_bar = np.ones(Npar) * (1.0/Npar) # the running average weights of the particles 
        #self.w_history = np.zeros((T, Npar))    # history of the weights
        #self.w_bar_history = np.zeros((T, Npar)) # history of the runninv average weights
    
    
    def init_particles(self):
        """
        Initialize the set of particles. 
        """
        
        # Method 1: Each particle is a dimension-K vector. We generate each particle 
        # uniformly at random from the space [0,1]^K. 
        # This method for any integer K.
        self.Particles = np.random.uniform(0, 1, (self.Npar, self.K))
        #print("Particles: ", self.Particles)
        
        
        # Method 2: We generate m points on [0,1] uniformly at random and let the set
        # of particles be the K-fold meshgrid of these m points. 
        # E.g. If m = 3 and the points are [0.1, 0.4, 0.7]. 
        # Then for K = 2, the particles are [0.1, 0.1], [0.1, 0.4], [0.1, 0.7],
        # [0.4, 0.1], [0.4, 0.4], [0.4, 0.7], [0.7, 0.1], [0.7, 0.4], [0.7, 0.7].
        # This method requires Npar = m^K.
        
                
        return None    
    
    
    def select_action(self, t):
        """
        Use Particle Thompson Sampling to select an action.
          
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:    the action, a numpy array of integers in [K] of shape (M,) 
        """
        
        theta_hat = self.generate_parameter_sample()
        #print('theta_hat:', theta_hat)
        
        a = aux.argmax_M_of_array(theta_hat, self.M)
        #print('Actual Action:', a)
        
        return a 
    
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action, a numpy array of integers in [K] of shape (M,)
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
          a:    the action, a numpy array of integers in [K] of shape (M,)
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
        
        #print('Particle weigths =', self.w)
        
        self.update_w_history(self.w, t)
        return None    
    
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        
        Input:
          t:    the round index, 0 <= t <= T-1. 
        """    
        
        self.w_bar = self.w_bar * (float(t)/(t+1)) + self.w / float(t+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None


    def update_w_history(self, w, t):
        """        
        Input:
          w:      the weights of the particles in round t, a probability vector of length Npar. 
          w_bar:  the running average weights of the particles in round t, a probability vector of length Npar.
          t:      the round index, 0 <= t <= T-1. 
        """        
        #self.w_history[t, :] = w
        return None    


    def update_w_bar_history(self, w_bar, t):
        """        
        Input:
          w_bar:  the running average weights of the particles in round t, a probability vector of length Npar.
          t:      the round index, 0 <= t <= T-1. 
        """        
        #self.w_bar_history[t, :] = w_bar
        return None  
    
    
    def print_state(self):
        """
        Print the current value of the state variables."
        """
        
        print('Particles = ', self.Particles)
        print('Weights = ', self.w)  
        return None


    def generate_parameter_sample(self):
        """
        Generate a sample theta_hat (one particle) based on the current weights on the particles. 
        
        Input:
          G:   a game system object. 
        
        Output:
          theta_hat: a length-K vector of values in [0,1].
        """   
        
        theta_hat = np.zeros(self.K) 
        k = np.random.choice(self.Npar, 1, p=self.w)[0]  # np.random.choice outputs an array
        theta_hat = self.Particles[k]   
        # ZEYU: is there a quicker way to implement this?
        return theta_hat










if __name__ == "__main__":
    pass