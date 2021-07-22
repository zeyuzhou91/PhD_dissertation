"""
In this module, Thompson sampling is implemented as a sub-class of the game.System class. 
"""

import numpy as np
import bandit
import auxiliary as aux


class System_TS(bandit.System): 
    
    def __init__(self, K, T):
        super().__init__(K, T) 
        self.Alpha = np.ones(K) # The alpha values of the arms
        self.Beta = np.ones(K)  # The beta values of the arms    
        self.theta_hat = np.zeros(K)    # The sampled parameter    
        
    def select_action(self, t):
        """
        Use Thompson Sampling to select an action.
        
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:   an action, an integer in [K]
        """
        
        self.theta_hat = self.generate_parameter_sample()
        #print('theta_hat:', self.theta_hat)
          
        a = aux.argmax_of_array(self.theta_hat) 
        #print('Actual Action:', a)
        return a 


    def generate_parameter_sample(self):
        """
        Generate a sample theta_hat based on the current posterior distribution of the parameter.   
        
        Output:
          theta_hat: a vector of values in [0,1], of length-K
        """   
    
        return np.random.beta(self.Alpha, self.Beta)

    
    def update_state(self, a, obs, t):
        """
        Update the Alpha and Beta arrays given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """       
               
        if obs == 1:
            self.Alpha[a] += 1
        else:
            self.Beta[a] += 1 
            
        #self.print_state()
        return None        



