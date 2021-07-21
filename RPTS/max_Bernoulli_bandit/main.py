"""
Simulation setup. 
"""

import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
import PTS
import RPTS
import pickle


np.set_printoptions(precision=4)


def run_simulations(K, M, T, Npar, N_simul, alg):
    
    x = np.zeros(T)
    y = np.zeros(T)
    for i in range(N_simul):
        if i % 1 == 0:
            print(str(K)+'-Arm, Choose ' + str(M) + ', ' + alg + ', Npar=' + str(Npar) + ' Simulation ', i)
            
        if alg == 'PTS':
            G = PTS.System_PTS(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG         

        if alg == 'RPTS1':
            G = RPTS.System_RPTS1(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG          

        if alg == 'RPTS2':
            G = RPTS.System_RPTS2(K,M,T,Npar)
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
    K = 10          # number of total arms
    M = 3           # number of arms to be chosen at each time step
    T = 10000      # time horizon
    N_simul = 10   # number of simulations   
    
    alg = 'PTS'
    Npar= 100   
    (x1,y1) = run_simulations(K,M,T,Npar,N_simul,alg)

    alg = 'RPTS1'
    Npar= 100   
    (x2,y2) = run_simulations(K,M,T,Npar,N_simul,alg)
    
    alg = 'RPTS2'
    Npar= 100   
    (x3,y3) = run_simulations(K,M,T,Npar,N_simul,alg) 
    
    plt.figure(1)
    plt.plot(range(T), x1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), x2, color='blue', linestyle='-', label = "PRTS-1, Npar=100")
    plt.plot(range(T), x3, color='green', linestyle='-', label = "PRTS-2, Npar=100")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('accumulative regret')
    plt.show()    
    
    plt.figure(2)
    plt.plot(range(T), y1, color='orange', linestyle='-', label = "PTS, Npar=100")
    plt.plot(range(T), y2, color='blue', linestyle='-', label = "PRTS-1, Npar=100")
    plt.plot(range(T), y3, color='green', linestyle='-', label = "PRTS-2, Npar=100")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('running average regret')
    plt.show()    