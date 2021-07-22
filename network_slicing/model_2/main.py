import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
import PTS
import RPTS
import pickle


np.set_printoptions(precision=4)
np.seterr(divide='raise')

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
    D = 3         # number of domains
    B = [3,3,3]   # number of resource blocks in each domain
    T = 1000      # time horizon
    N_simul = 10   # number of simulations
    
    alg = 'PTS_a'
    Npar= 100
    (x1,y1) = run_simulations(D,B,T,Npar,N_simul,alg)
    
    alg = 'PTS_b'
    Npar= 100
    (x2,y2) = run_simulations(D,B,T,Npar,N_simul,alg)    

    alg = 'RPTS2_a'
    Npar= 100
    (x3,y3) = run_simulations(D,B,T,Npar,N_simul,alg)    
    
    alg = 'RPTS2_b'
    Npar= 100
    (x4,y4) = run_simulations(D,B,T,Npar,N_simul,alg)
    
    
    plt.figure(1)
    plt.plot(range(T), x1, color='orange', linestyle='-', label = "PTS with 100 per-system particles")
    plt.plot(range(T), x2, color='purple', linestyle='-', label = "PTS with 100 per-block particles")
    plt.plot(range(T), x3, color='green', linestyle='-', label = "RPTS-2 with 100 per-system particles")
    plt.plot(range(T), x4, color='blue', linestyle='-', label = "RPTS-2 with 100 per-block particles")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('accumulative regret')
    plt.show()    
    
    plt.figure(2)
    plt.plot(range(T), y1, color='orange', linestyle='-', label = "PTS with 100 per-system particles")
    plt.plot(range(T), y2, color='purple', linestyle='-', label = "PTS with 100 per-block particles")
    plt.plot(range(T), y3, color='green', linestyle='-', label = "RPTS-2 with 100 per-system particles")
    plt.plot(range(T), y4, color='blue', linestyle='-', label = "RPTS-2 with 100 per-block particles")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('running average regret')
    plt.show()

     
    
    



      

       
