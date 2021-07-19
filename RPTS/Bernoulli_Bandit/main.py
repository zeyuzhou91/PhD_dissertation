"""
Simulation setup. 
"""


import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
from copy import copy
import Thompson_Sampling as TS
import PTS
import RPTS
import pickle


np.set_printoptions(precision=4)


def run_simulations(K, T, Npar, N_simul, alg):
    
    x = np.zeros(T)
    y = np.zeros(T)
    for i in range(N_simul):
        if i % 1 == 0:
            print(str(K)+'-Arm, ' + alg + ', Npar=' + str(Npar) + ' Simulation ', i)
        
        if alg == 'TS':
            G = TS.System_TS(K,T)
            G.init_true_parameter()
            G.find_best_action()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
        
        if alg == 'PTS':
            G = PTS.System_PTS(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'RPTS1':
            G = RPTS.System_RPTS1(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'RPTS2':
            G = RPTS.System_RPTS2(K,T,Npar)
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
    
    ## Set up model parameters
    K = 2         # number of arms
    T = 10000       # time horizon
    N_simul = 20   # number of simulations
    
    alg = 'PTS'    
    Npar = 100    # number of particles
    (x1,y1) = run_simulations(K,T,Npar,N_simul,alg)    
    
    alg = 'RPTS1'    
    Npar = 100    # number of particles
    (x2,y2) = run_simulations(K,T,Npar,N_simul,alg)   
    
    alg = 'RPTS2'    
    Npar = 100    # number of particles
    (x3,y3) = run_simulations(K,T,Npar,N_simul,alg)   
    
    alg = 'TS'   
    Npar = 100    # number of particles
    (x4,y4) = run_simulations(K,T,Npar,N_simul,alg)    
  
    plt.figure(1)
    plt.plot(range(T), x1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), x2, color='green', linestyle='-', label = "PRTS-1, Npar=100")
    plt.plot(range(T), x3, color='blue', linestyle='-', label = "PRTS-2, Npar=100")
    plt.plot(range(T), x4, color='red', linestyle='-', label = "TS")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('accumulative regret')
    plt.show()    
    
    plt.figure(2)
    plt.plot(range(T), y1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), y2, color='green', linestyle='-', label = "PRTS-1, Npar=100")
    plt.plot(range(T), y3, color='blue', linestyle='-', label = "PRTS-2, Npar=100")
    plt.plot(range(T), y4, color='red', linestyle='-', label = "TS")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('running average regret')
    plt.show()
  
   
    

    
       