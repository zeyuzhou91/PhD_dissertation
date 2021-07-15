import numpy as np
import scipy as sp
import scipy.stats as st


def argmax_of_array(array):
    """
    Find the index of the largest value in an array of real numbers. 
    
    Input:
      array:  an array of real numbers. 
    
    Output:
      index:  an integer in [K], where K = len(array)
    """
    
    # Simple but does not support random selection in the case of more than one largest values. 
    ind = np.argmax(array)
    return ind


def argmax_multi_domain_with_context(G, theta_hat, c):
    """
    Find the best action in the multi-domain network slicing problem, given context c
    and assuming the system parameter is theta_hat. 
    
    Input:
      theta_hat:  a numpy array of dimension (D, max(B), 3).
      c:          the context, a vector of length 3. 
    
    Output:
      a:          an action, a length-D vector of integers
    """
    
    a = np.zeros(G.D)
    for i in range(G.D):
        #print('shape of c: ', np.shape(c))
        #print('theta_hat[i]: ', theta_hat[i][:G.B[i]])
        #print('shape of theta_hat[i]: ', np.shape(theta_hat[i][:G.B[i]]))
        mu = theta_hat[i][:G.B[i]].dot(c)   # the vector of mu's in domain i
        #print('mu =', mu)
        a[i] = int(np.argmax(mu))
        #print('a[i] =', a[i])
    
    return a


def argmax_model2(G, theta_hat, c):
    """
    Find the best action in Model 2, given context c and assuming the 
    system parameter is theta_hat. 
    
    CAVEAT: this function only works with D=3. 
    
    Input:
      theta_hat:  the sampled system parameter, a numpy array of dimension (D, max(B), 2)
      c:          the context, a length-2 numpy array in [0,1]^2
    
    Output:
      a:          an action, a length-D vector of integers
    """
    
    arms = np.stack(np.meshgrid(range(G.B[0]),range(G.B[1]),range(G.B[2])), axis=-1).reshape(-1,G.D)
    #print('arms =', arms)
    tot_num_arms = G.B[0] * G.B[1] * G.B[2]
    E_rewards = np.zeros(tot_num_arms)
    for i in range(tot_num_arms):
        E_rewards[i] = calculate_expected_reward(G, arms[i], theta_hat, c)  
    ind = np.argmax(E_rewards)
    a = arms[ind]
    return a


def calculate_expected_reward(G, a, theta, c):
    """
    Calculate the expected reward by playing arm a, given context c, under system
    parameter theta. 
    
    Input:
      a:          an action/arm, a length-D vector of integers
      theta:      a numpy array of dimension (D, max(B), 2)
      c:          the context, a length-2 numpy array in [0,1]^2 
    """
    
    ## Method 1: Monte-Carlo
    #scales = np.zeros(G.D)
    #for i in range(G.D):
        #scales[i] = theta[i][int(a[i])][0] * c[0] + theta[i][int(a[i])][1]
    ##print('scales =', scales)
    #num_MC = 10000
    #tot_delay_MC = np.zeros(num_MC)
    #for i in range(G.D):
        ##print('tot_delay_MC =', tot_delay_MC)
        #domain_i_delay_MC = np.random.exponential(scales[i], num_MC)
        #tot_delay_MC += domain_i_delay_MC
    #tot_delay = np.mean(tot_delay_MC)
    #expected_reward = g(c[1], tot_delay)
    
    
    # Method 2: Approximate the total delay by a Gaussian r.v.
    scales = np.zeros(G.D)   # the means of exponential random variables 
    for i in range(G.D):
        scales[i] = theta[i][a[i]][0] * c[0] + theta[i][a[i]][1] 
    mu = sum(scales)   # the mean of the total delay
    var = sum(scales**2) # the variance of the total delay
    std = np.sqrt(var)
    r1 = (std/(c[1]*np.sqrt(2*np.pi))) * (np.exp(-mu**2/(2*var)) - np.exp(-(c[1]-mu)**2/(2*var)))
    r2 = (mu/c[1]) * (st.norm.cdf((c[1]-mu)/std) - st.norm.cdf(-mu/std))
    expected_reward = r1+r2
    
    return expected_reward


def g(c, y):
    """
    The g function used to evaluate the reward function. 
    
    c:    a positive value, the second coordinate of the context vector, the requested delay
    y:    a positive value, the actual end-to-end system delay
    """
        
    if 0 <= y <= c:
        result = y/c
    else:
        result = 0
    
    return result
    


def map_to_domain(x):
    """
    Map each number in the given array to [0,1]^K, if it is outside of that interval. 
    
    Input:
      x:  an numpy array of shape (N,K)
    
    Output:
      y:  an numpy array of shape (N,K)
    """
    
    lb = 1e-6
    #print('Before mapping, x=', x)
    y = np.copy(x)
    
    if np.ndim(x) == 1:
        (N,) = np.shape(x)
        for i in range(N):
            if y[i] <= 0:
                y[i] = lb
            elif y[i] > 1:
                y[i] = 1
            else:
                pass
     
    elif np.ndim(x) == 2:
        (N,K) = np.shape(x)
        for i in range(N):
            for j in range(K):
                if y[i][j] <= 0:
                    y[i][j] = lb
                elif y[i][j] > 1:
                    y[i][j] = 1
                else:
                    pass
    
    #print('After mapping, y=', y)       
    return y