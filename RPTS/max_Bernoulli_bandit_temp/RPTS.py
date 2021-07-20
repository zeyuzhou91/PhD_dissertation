import numpy as np
import scipy as sp
import scipy.stats as st
import Particle_Thompson_Sampling as PTS
import auxiliary as aux
import random



class System_PR1(PTS.System_PTS): 
    """
    Whenever 50% of the particles die, delete these dead particles, regenerate an equal
    number of particles uniformly at random from [0,1]^K, then reset the weights of all
    particles to 1/Npar.
    
    Definition of "50% of the particles die": the total weight of the lowest weighted 50% particles 
    is less than 0.01. That is, the remaining 50% particles take more than 99% of the total weight. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.01 
        self.check_frac = 0.5     # check this fraction of particles
        self.tau = 0                   # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = aux.argmin_of_array(self.w, die)  # indices of particles to be killed
        self.Particles[idx[:die]] = oblivious_exploration(self, die)  # particles killed and regenerated
        self.w = reweight_with_balancing(self)
        
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None 




class System_PR2(PTS.System_PTS): 
    """
    Same to PR1, except that the new particles are generated according to a Gaussian distribution
    with the empirical weighted mean and covariance matrix of the current particles. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.01 
        self.check_frac = 0.5     # check this fraction of particles
        self.tau = 0                   # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = aux.argmin_of_array(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        tra = np.trace(cov)
        #print('tra =', tra)
        
        #print('Particles =', self.Particles)
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, tra*np.eye(self.K))
        self.w = reweight_with_balancing(self)
        
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None




class System_PR3(PTS.System_PTS): 
    """
    Same to PR2, except the mean and covariance matrix of the regenerating Gaussian distribution 
    is not based on the weighted particles, but based on the surviving particles with equal weights. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.01 
        self.check_frac = 0.5     # check this fraction of particles
        self.tau = 0                   # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = aux.argmin_of_array(self.w, die)  # indices of particles to be killed
        
        # mu and cov are computed based on the surviving particles
        # and assuming they have equal weights
        sur = self.Npar-die
        (mu, cov) = calculate_empirical_stats(np.ones(sur)*(1.0/sur), self.Particles[idx[die:]])
        #print('mu =', mu)
        #print('cov =', cov)
        tra = np.trace(cov)
        #print('tra =', tra)
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, tra*np.eye(self.K))
        self.w = reweight_with_balancing(self)
        
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None


    
    
class System_PR4(PTS.System_PTS): 
    """
    No Survivor Rebalancing + Oblivious Exploration
    
    This algorithm is similar to PR1, with the following difference. After a regeneration, instead of resetting
    the weights of all particles, we remain the weights of the survived particles, except with a slight scaling down
    to leave room for a small and fixed weight for the re-generated particles. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar) 
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            #print('New epoch at t=', t)
            self.epochs.append(t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """           
    
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = aux.argmin_of_array(self.w, die)  # indices of particles to be killed
        
        self.Particles[idx[:die]] = oblivious_exploration(self, die)  
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None    
    


class System_PR5(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Guided Exploration
    
    Specifically: new particles are generated according to a Gaussian distribution, 
    where the mean and variance are empirically computed based on the weighted
    survivors before regeneration. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = aux.argmin_of_array(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        #print('diag(Cov) =', cov.diagonal())
        tra = np.trace(cov)
        #print('tra =', tra)  

        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, tra*np.eye(self.K))
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None

    
class System_PR6(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Guided Exploration
    
    Specifically: new particles are generated according to a Gaussian distribution, 
    where the mean and variance are empirically computed based on the un-weighted
    survivors before regeneration. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar) 
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        # mu and cov are computed based on the surviving particles
        # and assuming they have equal weights
        sur = self.Npar-die
        (mu, cov) = calculate_empirical_stats(np.ones(sur)*(1.0/sur), self.Particles[idx[die:]])
        #print('mu =', mu)
        #print('cov =', cov)
        tra = np.trace(cov)
        #print('tra =', tra)
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, tra*np.eye(self.K)) # particles killed and regenerated
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None
    


class System_PR7(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Guided Exploration
    
    Specifically: new particles are generated according to a Gaussian distribution, 
    where the mean and variance are empirically computed based on the weighted
    survivors before regeneration. 
    
    Difference between PR5 and PR7: In PR5, the covariance matrix is identity matrix
    multiplied by the trace of the empirical covariance matrix; in PR7, the covariance 
    matrix is the empirical covariance matrix itself. 
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        #print('diag(Cov) =', cov.diagonal())
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, cov) # particles killed and regenerated
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None



class System_PR7a(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Guided Exploration
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        #print('diag(Cov) =', cov.diagonal())
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, self.K * cov) # particles killed and regenerated
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None



class System_PR8(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Guided Exploration
    
    Compared to PR5, scale the trace by 1/K.
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar)
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            #print('New epoch at t=', t)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        tra = np.trace(cov) / self.K    # Compared to PR5, adding this 1/k factor
        #print('tra =', tra)  
        
        self.Particles[idx[:die]] = guided_Gaussian_exploration(self, die, mu, tra*np.eye(self.K)) # particles killed and regenerated
        self.w = reweight_without_balancing(self, die, idx)
        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None


class System_PR9(PTS.System_PTS): 
    """
    No Survivor Re-balancing + Hybrid Exploration
    """
    
    def __init__(self, K, M, T, Npar):
        super().__init__(K, M, T, Npar) 
        self.paralyze_threshold = 0.001   # if check_frac fraction of the lowest weighted particles have weights less than this value, regenerate.
        self.check_frac = 0.8            # check this fraction of particles
        self.rebirth_weight = 0.01        # the aggregate weight assigned to the re-generated particles
        self.epochs = [0]                  # the list of beginning times of epoches
        self.tau = 0                     # time since the beginning of the current epoch
        self.n_epo = 1.0                 # the number of epoches so far
        
    
    def update_state(self, a, obs, t):
        """
        Update the state variables given action a and observation obs. 
        
        Input:
          a:    the action taken in round t, an integer in [K]
          obs:  the observation incurred in round t, 0 or 1
          t:    the round index, 0 <= t <= T-1. (not used here)
        """
        
        self.update_weights(a, obs, t)   # only update weights, not particles 
        
        if is_paralyzed(self.w, int(self.Npar*self.check_frac), self.paralyze_threshold):
            self.kill_and_regenerate_particles(t)
            self.tau = 0   # a new epoch begins, reset tau
            self.epochs.append(t)
            self.n_epo += 1.0
            #print('New epoch at t= ', t)
            #print('n_epo= ', self.n_epo)
        else:
            self.tau += 1
            
        self.update_running_average_weights(t) 
        return None
    

    def kill_and_regenerate_particles(self, t):
        """
        Kill and regenerate the particles. 
        """    
        
        die = int(self.Npar * self.check_frac)  # kill this number of particles
        idx = np.argpartition(self.w, die)  # indices of particles to be killed
        
        (mu, cov) = calculate_empirical_stats(self.w, self.Particles)
        #print('mu =', mu)
        #print('cov =', cov)
        tra = np.trace(cov) / self.K   
        #print('tra =', tra) 
        Sigma = tra*np.eye(self.K)
        
        for i in range(die):
            if random.uniform(0,1) <= (1/self.n_epo):  # Oblivious Explore, PR4
                self.Particles[idx[i]] = oblivious_exploration(self, 1)
            else:   # Guided Explore, PR8
                self.Particles[idx[i]] = guided_Gaussian_exploration(self, 1, mu, Sigma)
        
        self.w = reweight_without_balancing(self, die, idx)

        return None
   
    
    def update_running_average_weights(self, t):
        """
        Update the running average weights of the particles.  
        """    
        
        # At an epoch, the running average weights need to be updated according to the current time 
        # counting from the most recent epoch, not from the beginning of time 

        if self.tau == 0:
            self.w_bar = self.w
        else:
            self.w_bar = self.w_bar * (float(self.tau)/(self.tau+1)) + self.w / float(self.tau+1) 
        #print('Running average particle weigths =', self.w_bar)
        
        self.update_w_bar_history(self.w_bar, t)
        return None



    
def is_paralyzed(v, num, threshold):
    """
    Decide if the num lowest valued entries in vector v add up to less than threshold. 
    
    Input:
       v:     a weight vector, a numpy array. 
       num:   an integer. 
       threshold:  a decimal number in [0,1], typically small. 
       
    Output:
      True or False.
    """

    w = np.copy(v)    # make a copy of v without reference
    w.sort()          # sort w from smallest value to largest value
    val = sum(w[:num])
    if val < threshold:
        return True
    else:
        return False    
    
       
#x = np.array([1,9,3,4,3,6,7,8,6,10])
#print(is_paralyzed(x, 3, 0.5))
#y = np.array([0.5, 0.001, 0.2, 0.0001, 0.0002, 0.0003, 0.2, 0.1, 0, 0])
#print(is_paralyzed(y, 3, 0.1))


def oblivious_exploration(G, n):
    """
    Generate n particles uniformly at random from the parameter space of the game. 
    
    Inputs:
      G: the game instance.
      n: an integer, generate this number of particles. 
    
    Output:
      Par: an numpy array of dimension (n, G.K), where each row is a particle. 
    """
    
    Par = np.random.uniform(0, 1, (n, G.K))
    return Par


def guided_Gaussian_exploration(G, n, mu, Sigma):
    """
    Generate n particles according to Gaussian(mu, Sigma).
    
    Inputs:
      G: the game instance.
      n: an integer, generate this number of particles. 
      mu:  the mean of the Gaussian distribution.
      Sigma:  the covariance matrix of the Gaussian distribution. 
    
    Output:
      Par: an numpy array of dimension (n, G.K), where each row is a particle. 
    """
    
    Par = aux.map_to_domain(np.random.multivariate_normal(mu, Sigma, n))
    return Par


def reweight_without_balancing(G, n, idx):
    """
    Re-set the particle weight vector. Give the entries at idx[:n] a total weight of G.rebirth_weight. 
    Scale other entries so that all entries still add up to one.
    
    Inputs:
      n:  an integer, the weights of this number of entries need to be reset. 
      idx: a numpy array of integers, the index array.
      
    Output:
      w:  a numpy array, the updated weight vector. 
    """
    
    w = np.copy(G.w)
    w[idx[:n]] = np.ones(n) * (G.rebirth_weight/n)               #  weights of the re-generated particles: total weight = rebirth_weight
    w[idx[n:]] *= (1-G.rebirth_weight) / (sum(w[idx[n:]]))       # weights of the survived particles: total weight = 1-rebirth_weight 
    return w


def reweight_with_balancing(G):
    """
    Re-set the weights of the particles to be equal to each other. 
      
    Output:
      w:  a numpy array, the weight vector. 
    """
    
    w = np.ones(G.Npar) * (1.0/G.Npar)
    return w
    
    
def calculate_empirical_stats(w, X):
    """
    Calculate the empirical mean and covariance matrix of the data in X with respect to weights w. 
    
    Inputs:
      w: a numpy array, a weight vector of shape (N,).
      X: a numpy array, shape (N,K)
      
    Outputs:
      mu: a numpy array of shape (K,)
      cov: a numpy array of shape (K,K) 
      
    Example:
    w = [w1 w2 w3 w4 w5]   N=5
    X = [x1   x2]
      = [x11  x21
         x12  x22
         x13  x23
         x14  x24
         x15  x25]
    K=2
    
    mu = [E[x1] E[x2]] is the weighted average of the 5 row vectors
    cov = [E[x1^2]  E[x1*x2]
           E[x2*x1] E[x2^2]]
    where all the expectations are with respect to the weight w. 
    
    Example:
    w = [0.2 0.3 0.5]
    X = [1 2
         3 1
         4 4]
    
    then
    mu = [3.1 2.7]
    cov = [1.29 0.93
           0.93 1.81]
    """
    
    (N,) = np.shape(w)
    #print('N =', N)
    #print('np.shape(w) =', np.shape(w))
    
    mu = w.dot(X)
    #print('mu =', mu)
    #print('np.shape(mu) =', np.shape(mu))

    Y = X-mu    # Y is the shifted version of X with mean zero
    #print('Y =', Y)
    
    v = np.sqrt(w)  # the element-wise square-root of w
    v = v.reshape(N,1)  # reshape into a column vector
    #print('v =', v)
    
    Z = v*Y         # element-wise scaling of each column of Y
    cov = Z.T.dot(Z)
    #print('cov =', cov)
    #print('np.shape(cov) =', np.shape(cov))
    return (mu, cov)


#w = np.array([0.2, 0.3, 0.5])
#X = np.array([[1,2], [3,1], [4,4]])
#calculate_empirical_stats(w, X)
    
    
    