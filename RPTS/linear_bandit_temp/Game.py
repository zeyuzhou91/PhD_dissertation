import numpy as np
import scipy as sp
import scipy.stats as st
import auxiliary as aux
import myplot


class System:
    def __init__(self, N, var_W, T):
        
        self.N = N          # dimension of the parameter space
        self.var_W = var_W  # variance of the noise W
        self.T = T          # time horizon       
        self.theta_true = np.zeros(N)   # The true system parameter 
        self.best_action = np.zeros(N)  # The best action
        self.best_reward = 0            # The expected reward corresponding to the best action
                
        # History
        self.A = np.zeros((T, N))    # the action history  # Note that self.A[t,:] is the action taken at time t, which is stored here as a row vector.
        self.OBS = np.zeros(T)       # the observation history
        self.REW = np.zeros(T)       # the reward history   
        self.REG = np.zeros(T)       # the regret history  
        self.CUM_REG = np.zeros(T)   # the cumulative regret history
        self.AVG_REG = np.zeros(T)   # the running average regret history       
    
    
    def init_true_parameter(self):
        """
        Initialize the true system parameter. 
        """    
        
        #self.theta_true = np.random.uniform(-1,1,self.N)   
        #self.theta_true = aux.generate_uniform_points_in_ball(1, 1, self.N)
        self.theta_true = np.array([0.5, 0.5])
        #print('theta_true =', self.theta_true)
        
        return None     


    def play(self, a, t):
        """
        Given action a, generate observation, record/calculate the reward and regret. 
        
        Input:
          a:    the action, a length-N numpy array 
          t:    the round index, 0 <= t <= T-1.
        
        Output:
          obs:  the observation, a single value
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
            a:    the action, a length-N numpy array 
            
        Output:
            obs:  the observation, a scaler
        """        
        
        mean = a.dot(self.theta_true)
        # the mean must be 1 dimensional and the covariance matrix 2 dimensional
        obs = np.random.multivariate_normal(np.array([mean]), np.array([[self.var_W]]))
        return float(obs)


    def find_best_action(self):
        """
        Find the best action/arm of the system based on the current parameters. 
        """
        
        self.best_action = self.theta_true / np.linalg.norm(self.theta_true)
        #print('best action: ', self.best_action)
        #print('np.shape(best_action) =', np.shape(self.best_action))
        #print('np.shape(theta_true) =', np.shape(self.theta_true))
        self.best_reward = self.best_action.dot(self.theta_true)
        #print('best reward: ', self.best_reward)
        return None


    def calculate_reward(self, a):
        """        
        Given the action a, calculate the reward. 
        Note that the reward doesn't depend on the observation in this setting.
        
        Input:
            a:   the actual action, a length-N numpy array
            
        Output:
            reward: a real value.  
        """
        
        # The actual reward is usually a function of the observation. 
        # However, here we consider the expected reward, which is a function of the action.
        
        reward = a.dot(self.theta_true)     
      
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
            
            # plot the current states
            #myplot.plot_figures(self, t)
              
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
          a:    the action, a length-N numpy array
          obs:  the observation, a scaler
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
