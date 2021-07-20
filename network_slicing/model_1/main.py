import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
from copy import copy
import PTS
import RPTS
import pickle



np.set_printoptions(precision=4)

def run_simulations(D, B, T, Npar, N_simul, alg):
    
    x = np.zeros(T)
    y = np.zeros(T)
    for i in range(N_simul):
        if i % 1 == 0:
            print(alg + ', Npar=' + str(Npar) + ' Simulation ', i)
        
        if alg == 'PTS_a':
            Npar_sys = Npar
            G = PTS.System_PTS_a(D,B,T,Npar_sys)
            G.init_true_parameter()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            
        if alg == 'PTS_b':
            Npar_blk = Npar
            G = PTS.System_PTS_b(D,B,T,Npar_blk)
            G.init_true_parameter()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG           

        if alg == 'RPTS2_a':
            Npar_sys = Npar
            G = RPTS.System_RPTS2_a(D,B,T,Npar_sys)
            G.init_true_parameter()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'RPTS2_b':
            Npar_blk = Npar
            G = RPTS.System_RPTS2_b(D,B,T,Npar_blk)
            G.init_true_parameter()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

    x = x / N_simul
    y = y / N_simul
    return (x, y)

       
if __name__ == "__main__":
    
    # Set up model parameters
    D = 3        # number of domains
    B = [3,3,3]  # number of resource blocks in each domain
    T = 10000      # time horizon
    N_simul = 10  # number of simulations
    
    alg = 'PTS_b'
    Npar= 100
    (x,y) = run_simulations(D,B,T,Npar,N_simul,alg)
    fw = open('data/network_slicing_model1_' + str(B[0]) + '_' + str(B[1]) + '_' + str(B[2]) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    pickle.dump(x, fw)
    fw.close()
    fw = open('data/network_slicing_model1_' + str(B[0]) + '_' + str(B[1]) + '_' + str(B[2]) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    pickle.dump(y, fw)
    fw.close()
    
    
    #alg = 'PTS_b'
    #Npar= 100
    #(x,y) = run_simulations(D,B,T,Npar,N_simul,alg)
    #fw = open('data/network_slicing_model1_' + str(B[0]) + '_' + str(B[1]) + '_' + str(B[2]) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    #pickle.dump(x, fw)
    #fw.close()
    #fw = open('data/network_slicing_model1_' + str(B[0]) + '_' + str(B[1]) + '_' + str(B[2]) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    #pickle.dump(y, fw)
    #fw.close()      
    
    
    
    
    