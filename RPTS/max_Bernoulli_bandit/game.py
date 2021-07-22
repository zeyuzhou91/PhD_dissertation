"""
In this module, the class System is defined, which contains the variables and 
procedures of the bandit problem, a sequence decision game. 
"""


import numpy as np
import auxiliary as aux


class System:
    def __init__(self, K, M, T):
        
        self.K = K          # number of arms
        self.M = M          # number of arms seleted at each step
        self.T = T          # time horizon       
        self.theta_true = np.zeros(K)   # The true system parameter
        self.best_action = np.zeros(M, dtype=int)   # The best action
        self.best_reward = 0            # The expected reward corresponding to the best action        
                
        # History
        self.A = np.zeros((T, M))    # the action history  
        self.OBS = np.zeros(T)       # the observation history
        self.REW = np.zeros(T)       # the reward history   
        self.REG = np.zeros(T)       # the regret history  
        self.CUM_REG = np.zeros(T)   # the cumulative regret history  
        self.AVG_REG = np.zeros(T)   # the running average regret history      

    
    def init_true_parameter(self):
        """
        Initialize the true system parameter. 
        """    
        
        #self.theta_true = np.random.uniform(0,1,self.K) # randomly choose a parameter in [0,1]^K
        self.theta_true = np.array([0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
        #print('theta_true =', self.theta_true)
        
        return None     


    def play(self, a, t):
        """
        Given action a, generate observation, record/calculate the reward and regret. 
        
        Input:
          a:    the action, a numpy array of integers in [K] of shape (M,)
          t:    the round index, 0 <= t <= T-1.
        
        Output:
          obs:  the observation, 0 or 1
          rew:  the reward, a single value
          reg:  the regret, a single value 
        """
    
        # Play the game, get an observation
        obs = self.obtain_observation(a)
        
        # Performance measure   
        rew = self.calculate_reward(a)
        reg = self.calculate_regret(rew)  
        
        return (obs, rew, reg) 



    def obtain_observation(self, a):        
        """
        Given an action a, generate the observation, which is random.  
        
        Input:
            a:    the action, a numpy array of integers in [K] of shape (M,) 
            
        Output:
            obs:  the observation, 0 or 1
        """        
    
        selected_thetas = self.theta_true[a]
        #print('The selected theta values =', selected_thetas)
        values = np.random.binomial(1, selected_thetas)
        obs = max(values)        
        return obs
     

    def find_best_action(self):
        """
        Find the best action/arm of the system based on the current parameters. 
        """
        
        self.best_action = aux.argmax_M_of_array(self.theta_true, self.M)
        #print('best action: ', self.best_action)
        self.best_reward = self.calculate_reward(self.best_action)
        #print('best reward: ', self.best_reward)
        return None    
    
    
    def calculate_reward(self, a):
        """        
        Given the action a, calculate the reward. 
        Note that the reward doesn't depend on the observation in this setting.
        
        Input:
            a:    the action, a numpy array of integers in [K] of shape (M,)
            
        Output:
            reward: a real value.  
        """
        
        # The actual reward is usually a function of the observation. 
        # However, here we consider the expected reward, which is a function of the action.
        selected_thetas = self.theta_true[a]
        p = np.prod(1-selected_thetas)
        reward = 1-p    
      
        return reward
    

    def calculate_regret(self, actual_reward):
        """
        Calculate the regret of not choosing the best action, which equals to the
        reward of choosing the best action minus the actual reward. 
        
        Input:
            actual_reward: a real value. 
            
        Output:
            reg: the regret of not choosing the best action, a real value. 
        """
        
        reg = self.best_reward - actual_reward
        return reg


    def run(self):
        """
        Run the game. 
        """
        
        for t in range(self.T):
            #if t % 1 == 0:
                #print(t)
              
            # select an action
            a = self.select_action(t)
            #print('Action:', a)
      
            # Obtain observation, record/calculate the reward and regret  
            (obs, rew, reg) = self.play(a, t)
            #print('observation:', obs) 
            #print('reward:', rew)
            #print('regret:', reg)
            
            # update state variables 
            self.update_state(a, obs, t)       
            
            # update history
            self.update_history(a, obs, rew, reg, t)
        return None


    def update_history(self, a, obs, rew, reg, t):
        """        
        Input:
          a:    the action, a numpy array of integers in [K] of shape (M,)
          obs:  the observation, 0 or 1
          rew:  the reward, a single value
          reg:  the regret, a single value 
          t:    the round index, 0 <= t <= T-1. 
        """   
        self.A[t,:] = a  # action history
        self.OBS[t] = obs  # obsevation history
        self.REW[t] = rew  # reward history
        self.REG[t] = reg  # regret history
        if t == 0:         # accumulative regret history
            self.CUM_REG[t] = reg
        else:
            self.CUM_REG[t] = self.CUM_REG[t-1] + reg  
        self.AVG_REG[t] = self.CUM_REG[t] / float(t+1)  # running average regret history
        return None 
