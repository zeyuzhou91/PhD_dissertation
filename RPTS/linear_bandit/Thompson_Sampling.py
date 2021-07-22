import numpy as np
import bandit
import auxiliary as aux


class System_TS(bandit.System): 
    def __init__(self, K, var_W, T):
        super().__init__(K, var_W, T) 
        self.Sigma = np.eye(K)      # The variance matrix of the posterior (Normal) distribution of theta 
        self.gain = np.ones(K)  # The gain value in the update quation of theta_bar   # the initialization doesn't matter
        self.theta_hat = np.zeros(K)    # The sampled parameter
        self.theta_bar = np.zeros(K)  # The mean value of the posterior (Normal) distribution of theta  
            
    def select_action(self, t):
        """
        Use Thompson Sampling to select an action.
        
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:   an action, a length-K numpy array 
        """
        
        self.theta_hat = self.generate_parameter_sample()
        #print('theta_hat:', self.theta_hat)
        
        a = self.theta_hat/np.linalg.norm(self.theta_hat)
        #print('Actual Action:', a)
        
        #a = np.array([1.0, 0.0])
        return a 
    
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an length-K numpy array
          obs:  the observation incurred in round t, a scaler
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        b = a.reshape(self.K, 1)  # reshape dimension-K array a into a dimension-(K,1) array to facilitate matrix operation
        
        temp = float(b.T.dot(self.Sigma).dot(b)) + self.var_W
        #print('temp =', temp)
        
        self.gain = (self.Sigma.dot(b) / temp).reshape(self.K)
        #print('gain =', self.gain)
        
        self.Sigma = self.Sigma - self.Sigma.dot(b).dot(b.T).dot(self.Sigma) / temp
        #print('trace(Sigma) =', np.trace(self.Sigma))
        
        self.theta_bar = self.theta_bar + self.gain * (obs - float(b.T.dot(self.theta_bar)))
        #print('theta_bar =', self.theta_bar)
             
        return None    


    def print_state(self):
        """
        Print the current value of the state variables."
        """
        
        print('Sigma = ', self.Sigma)
        print('gain = ', self.gain)
        print('theta_bar = ', self.theta_bar)
        return None


    def generate_parameter_sample(self):
        """
        Generate a sample theta_hat based on the current posterior distribution of the parameter.   
        
        Output:
          theta_hat: a length-K numpy array
        """   
        
        #print('dimension of G.theta_bar =', self.theta_bar.ndim)
        return np.random.multivariate_normal(self.theta_bar, self.Sigma)
     
