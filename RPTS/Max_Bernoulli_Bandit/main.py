import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
import Particle_Thompson_Sampling as PTS
import Particle_Regeneration as PR
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
        
        if alg == 'PR1':
            G = PR.System_PR1(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR2':
            G = PR.System_PR2(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR3':
            G = PR.System_PR3(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR4':
            G = PR.System_PR4(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG            

        if alg == 'PR5':
            G = PR.System_PR5(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            
        if alg == 'PR6':
            G = PR.System_PR6(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG            

        if alg == 'PR7':
            G = PR.System_PR7(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG 
            
        if alg == 'PR7a':
            G = PR.System_PR7a(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG             

        if alg == 'PR8':
            G = PR.System_PR8(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

        if alg == 'PR9':
            G = PR.System_PR9(K,M,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG

            
    #print('theta_true =', G.theta_true)  
    
    x = x / N_simul
    y = y / N_simul
    return (x, y)
        

       
if __name__ == "__main__":
        
    ## Set up model parameters
    K = 10       # number of total arms
    M = 3       # number of arms to be chosen at each time step
    T = 200000      # time horizon
    #Npar = 10    # number of particles
    ##T_epoch = 4  # Epoch time 
    N_simul = 200   # number of simulations   
    
    alg = 'PTS'
    Npar=100   
    (x,y) = run_simulations(K,M,T,Npar,N_simul,alg)
    #fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + 'theta_0.51_to_0.60_' + alg + '_N' + str(Npar) + '_T200K_CUM', 'wb')
    pickle.dump(x, fw)
    fw.close()
    #fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + 'theta_0.51_to_0.60_' + alg + '_N' + str(Npar) + '_T200K_AVG', 'wb')
    pickle.dump(y, fw)
    fw.close()

    