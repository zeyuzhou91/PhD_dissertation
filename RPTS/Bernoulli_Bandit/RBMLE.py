import numpy as np
import scipy as sp
import scipy.stats as st
import Game
import auxiliary as aux



class System_RBMLE(Game.System): 
    def __init__(self, K, T):
        super().__init__(K, T)
        self.S = np.zeros(K)  # S[i] is the total number of sucesses (1's) by playing arm i so far
        self.F = np.zeros(K)  # F[i] is the total number of failures (0's) by playing arm i so far
        self.I = np.zeros(K)   # I[i] is the index value of arm i        
        
    def select_action(self, t):
        """
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:   an action, an integer in [K]
        """
        
        a = aux.argmax_of_array(self.I) 
        return a 

    
    def update_state(self, a, obs, t):
        """
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """       
               
        if obs == 1:
            self.S[a] += 1
        else:
            self.F[a] += 1 
            
        alp = 10*np.log(t+1)
        
        for a in range(self.K):
            N = self.S[a] + self.F[a]
            
            if N == 0:
                term1 = 0
                term2 = 0
            elif self.S[a]+alp == 0:
                term1 = 0
                term2 = self.F[a] * (np.log(N) - np.log(N+alp))
            else:
                term1 = (self.S[a]+alp) * (np.log(self.S[a]+alp) - np.log(N+alp))
                term2 = self.F[a] * (np.log(N) - np.log(N+alp))
            
            if self.S[a] == 0:
                term3 = 0
            else:
                term3 = self.S[a] * (np.log(N) - np.log(self.S[a]))
        
            self.I[a] = term1 + term2 + term3
            
        return None        
             
  
    def print_state(self):
        """
        Print the current value of the state variables."
        """
        
        return None    