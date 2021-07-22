"""
Simulation setup. 
"""

import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
import PTS
import Thompson_Sampling as TS
import RPTS


np.set_printoptions(precision=4)

def run_simulations(K, var_W, T, Npar, N_simul, alg):
    
    x = np.zeros(T)
    y = np.zeros(T)
    #start = time.time()
    for i in range(N_simul):
        if i % 1 == 0:
            print('Dimension-' + str(K) + ', ' + alg + ', Npar=' + str(Npar) + ' Simulation ', i)
         
        if alg == 'TS':
            G = TS.System_TS(K,var_W,T)
            G.init_true_parameter()
            G.find_best_action()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG         
            
        if alg == 'PTS':
            G = PTS.System_PTS(K,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'RPTS1':
            G = RPTS.System_RPTS1(K,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG 

        if alg == 'RPTS2':
            G = RPTS.System_RPTS2(K,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG            
    
    x = x / N_simul
    y = y / N_simul
    return (x, y)
        

    
if __name__ == "__main__":
    
    # Set up model parameters
    K = 2        # dimension of the parameter space
    var_W = 0.1  # variance of the noise W
    T = 10000      # time horizon
    N_simul = 10   # number of simulations  
    
    alg='PTS'
    Npar=100
    (x1,y1) = run_simulations(K,var_W,T,Npar,N_simul,alg)
    
    alg='RPTS1'
    Npar=100
    (x2,y2) = run_simulations(K,var_W,T,Npar,N_simul,alg) 
    
    alg='RPTS2'
    Npar=100
    (x3,y3) = run_simulations(K,var_W,T,Npar,N_simul,alg)      
    
    alg='TS'
    Npar=100
    (x4,y4) = run_simulations(K,var_W,T,Npar,N_simul,alg)     
    
    plt.figure(1)
    plt.plot(range(T), x1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), x2, color='blue', linestyle='-', label = "RPTS-1, Npar=100")
    plt.plot(range(T), x3, color='green', linestyle='-', label = "RPTS-2, Npar=100")
    plt.plot(range(T), x4, color='red', linestyle='-', label = "TS")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('accumulative regret')
    plt.show()    
    
    plt.figure(2)
    plt.plot(range(T), y1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), y2, color='blue', linestyle='-', label = "RPTS-1, Npar=100")
    plt.plot(range(T), y3, color='green', linestyle='-', label = "RPTS-2, Npar=100")
    plt.plot(range(T), y4, color='red', linestyle='-', label = "TS")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('running average regret')
    plt.show()    