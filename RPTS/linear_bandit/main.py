import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
from copy import copy
import Particle_Thompson_Sampling as PTS
import Thompson_Sampling as TS
import Particle_Regeneration as PR
import pickle
import time


np.set_printoptions(precision=4)

def run_simulations(N, var_W, T, Npar, N_simul, alg):
    
    x = np.zeros(T)
    y = np.zeros(T)
    #start = time.time()
    for i in range(N_simul):
        if i % 1 == 0:
            print('Dimension-' + str(N) + ', ' + alg + ', Npar=' + str(Npar) + ' Simulation ', i)
         
        if alg == 'TS':
            G = TS.System_TS(N,var_W,T)
            G.init_true_parameter()
            G.find_best_action()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG         
            
        if alg == 'PTS':
            G = PTS.System_PTS(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
        
        if alg == 'PR1':
            G = PR.System_PR1(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR2':
            G = PR.System_PR2(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR3':
            G = PR.System_PR3(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR4':
            G = PR.System_PR4(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR5':
            G = PR.System_PR5(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            
        if alg == 'PR6':
            G = PR.System_PR6(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG                

        if alg == 'PR7':
            G = PR.System_PR7(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG 

        if alg == 'PR7a':
            G = PR.System_PR7a(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            
        if alg == 'PR8':
            G = PR.System_PR8(N,var_W,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            
        if alg == 'PR9':
            G = PR.System_PR9(N,var_W,T,Npar)
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
    N = 2        # dimension of the parameter space
    var_W = 0.1  # variance of the noise W
    T = 1000      # time horizon
    #Npar = 200    # number of particles
    N_simul = 1   # number of simulations  
    
    alg='PR7'
    Npar=100
    (x,y) = run_simulations(N,var_W,T,Npar,N_simul,alg)
    #fw = open('data/D' + str(N) + '/Linear_D' + str(N) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    #pickle.dump(x, fw)
    #fw.close()
    #fw = open('data/D' + str(N) + '/Linear_D' + str(N) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    #pickle.dump(y, fw)
    #fw.close()
    
   