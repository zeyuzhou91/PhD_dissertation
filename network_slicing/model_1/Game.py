import numpy as np
import auxiliary as aux



class System:
    def __init__(self, D, B, T):
        
        self.D = D  # number of domains
        self.B = B  # number of resource blocks in each domain
        self.T = T  # time horizon       
        self.theta_true = np.zeros((D, max(B), 3))  # The true system parameter      
                
        # History
        self.C = np.zeros((T, 3))    # the context history
        self.A = np.zeros((T, D))    # the action history
        self.OBS = np.zeros((T, D))  # the observation history
        
        self.REW = np.zeros(T)       # the reward history   
        self.REG = np.zeros(T)       # the regret history  
        self.CUM_REG = np.zeros(T)   # the cumulative regret history
        self.AVG_REG = np.zeros(T)   # the running average regret history       
    
    
    def init_true_parameter(self):
        """
        Initialize the true system parameter. The parameter for each resource block
        is generated uniformly at random from the set of probability vectors of 
        length 3. 
        """    
        
        for i in range(self.D):
            for j in range(self.B[i]):
                p = np.random.uniform(0, 1, 3)  # a length-3 vector
                self.theta_true[i][j] = p/sum(p)   # normalize p to be a probability vector
        #print('theta_true =', self.theta_true)
        
        return None       


    def generate_context(self, t):
        """
        Generate a context. 
        
        Input: 
          t:    the round index, 0 <= t <= T-1. Not used. 
                  
        Output:
          c:   a length-3 numpy array in [0,1]^3.
        """
        
        c = np.random.uniform(0, 1, 3)
        return c


    def play(self, c, a, t):
        """
        Given context c, action a, generate observation, record/calculate the reward and regret. 
        
        Input:
          c:    the context, a numpy array in [0,1]^3
          a:    the action, a length-D vector of integers 
          t:    the round index, 0 <= t <= T-1.
        
        Output:
          obs:  the observation, a length-D binary vector
          rew:  the reward, a single value
          reg:  the regret, a single value 
        """
    
        # Play the game, get an observation
        obs = self.obtain_observation(c, a)
        
        # Performance measure
        best_action = self.find_best_action(c)
        #print('best_action is ', best_action)    
        rew = self.calculate_reward(c, a)
        reg = self.calculate_regret(c, rew, best_action)  
        
        return (obs, rew, reg) 



    def obtain_observation(self, c, a):        
        """
        Given an action a and context c, generate the observation, which is random.  
        
        Input:
            c:    the context, a numpy array in [0,1]^3
            a:    the action, a length-D vector of integers 
            
        Output:
            obs:  the observation, a binary length-D vector. 
        """        
        
        obs = np.zeros(self.D)
        for i in range(self.D):
            mu = self.theta_true[i][a[i]].dot(c)   # a probability, the parameter of a bernoulli dist.
            #print('mu =', mu)
            obs[i] = np.random.binomial(1, mu)
        return obs


    def find_best_action(self, c):
        """
        Find the best action/arm of the system based on the current parameters and the context c. 
        
        Input:
          c:   the context, a numpy array in [0,1]^3
        
        Output:
          a:   the action, a length-D vector of integers 
        """
        
        a = aux.argmax_multi_domain_with_context(self, self.theta_true, c)
        return a


    def calculate_reward(self, c, a):
        """        
        Given the context c and action a, calculate the reward. 
        Note that the reward doesn't depend on the observation in this setting.
        
        Input:
            c:   the context, a numpy array in [0,1]^3
            a:   the actual action, a length-D vector of integers 
            
        Output:
            reward: a real value.  
        """
        
        # The actual reward is usually a function of the observation. 
        # However, here we consider the expected reward, which is a function of the action and context.
        
        reward = 0.0
        for i in range(self.D):
            mu = self.theta_true[i][int(a[i])].dot(c)  
            reward += mu        
      
        return reward
    

    def calculate_regret(self, c, actual_reward, best_action):
        """
        Calculate the regret of not choosing the best action, which equals to the
        reward of choosing the best action minus the actual reward. 
        
        Input:
            c:   the context, a numpy array in [0,1]^3  
            best_action: the best action, a length-D vector of integers
            actual_reward: a real value. 
            
        Output:
            reg: the regret of not choosing the best action, a real value. 
        """
        
        best_reward = self.calculate_reward(c, best_action)
        reg = best_reward - actual_reward
        return reg


    def run(self):
        """
        Run the game. 
        """
        
        for t in range(self.T):
            #if t % 1 == 0:
                #print(t)
            
            # Generate a context
            c = self.generate_context(t)
            #print('Context: ', c)
                 
            # select an action
            a = self.select_action(t, c)
            #print('Action:', a)
      
            # Obtain observation, record/calculate the reward and regret  
            (obs, rew, reg) = self.play(c, a, t)
            #print('observation:', obs) 
            #print('reward:', rew)
            #print('regret:', reg)
            
            # update state variables 
            self.update_state(c, a, obs, t)       
            
            # update history
            self.update_history(c, a, obs, rew, reg, t)
        return None


    def update_history(self, c, a, obs, rew, reg, t):
        """        
        Input:
          c:    the context, a numpy array in [0,1]^3
          a:    the action, a length-D vector of integers  
          obs:  the observation, a binary length-D vector
          rew:  the reward, a single value
          reg:  the regret, a single value 
          t:    the round index, 0 <= t <= T-1. 
        """   
        self.C[t,:] = c  # context history
        self.A[t,:] = a  # action history
        self.OBS[t,:] = obs  # obsevation history
        self.REW[t] = rew  # reward history
        self.REG[t] = reg  # regret history
        if t == 0:         # accumulative regret history
            self.CUM_REG[t] = reg
        else:
            self.CUM_REG[t] = self.CUM_REG[t-1] + reg  
        self.AVG_REG[t] = self.CUM_REG[t] / float(t+1)  # running average regret history
        return None 
