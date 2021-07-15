import numpy as np
import Game
import auxiliary as aux



class System_UCB(Game.System): 
    def __init__(self, K, T):
        Game.System.__init__(self, K, T) 
        self.N = np.zeros(K)  # N[i] is the number of times arm i has been played so far
        self.S = np.zeros(K)  # S[i] is the total reward obtained from arm i so far
        self.avg = np.zeros(K)  #avg[i] is the average reward obtained from arm i so far
        self.I = np.ones(K) * float('inf')  # I[i] is the index value of arm i       
            
                
    def select_action(self, t):
        """
        Use the UCB (Upper Confidence Bound) algorithm to select an action. 
        
        Input:
          t:    the round index, 0 <= t <= T-1.
          
        Output:
          a:   an action/arm, an integer in [K]. 
        """
        
        a = aux.argmax_of_array(self.I) 
        
        self.update_action_history(a, t)
        return a    
    
    
    
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
        return None



    def update_state(self, a, obs, t):
        """
        Update the state variables based on action a and observation obs. 
        
        Input:
          a:    the action/arm taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.N[a] += 1
        self.S[a] += obs
        self.avg[a] = self.S[a] / float(self.N[a])
        
        for i in range(len(self.I)):
            if self.N[i] == 0:  # this arm has not been pulled
                pass
            else:
                self.I[i] = self.avg[i] + np.sqrt(2*np.log(t+1)/self.N[i])
        return None
    
        
    def print_state(self):
        """
        Print the current value of the state variables."
        """
        
        print('N = ', self.N)
        print('S = ', self.S)
        print('avg = ', self.avg)
        print('I = ', self.I)   
        return None



    

    
    
