import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
from copy import copy
import Thompson_Sampling as TS
import Particle_Thompson_Sampling as PTS
import Particle_Regeneration as PR
import RBMLE
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
            z = []
            
        if alg == 'RBMLE':
            G = RBMLE.System_RBMLE(K,T)
            G.init_true_parameter()
            G.find_best_action()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG 
            z = []
        
        if alg == 'PTS':
            G = PTS.System_PTS(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = []
        
        if alg == 'PR1':
            G = PR.System_PR1(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = []

        if alg == 'PR2':
            G = PR.System_PR2(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = []

        if alg == 'PR3':
            G = PR.System_PR3(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = []

        if alg == 'PR4':
            G = PR.System_PR4(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR5':
            G = PR.System_PR5(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs
            
        if alg == 'PR6':
            G = PR.System_PR6(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG  
            z = G.epochs

        if alg == 'PR7':
            G = PR.System_PR7(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR72':
            G = PR.System_PR7_2(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR73':
            G = PR.System_PR7_3(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR75':
            G = PR.System_PR7_5(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR7logt':
            G = PR.System_PR7_logt(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs


        if alg == 'PR7a':
            G = PR.System_PR7a(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = []

        if alg == 'PR8':
            G = PR.System_PR8(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

        if alg == 'PR8logt':
            G = PR.System_PR8_logt(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs


        if alg == 'PR9':
            G = PR.System_PR9(K,T,Npar)
            G.init_true_parameter()
            G.find_best_action()
            G.init_particles()
            G.run()
            x += G.CUM_REG
            y += G.AVG_REG
            z = G.epochs

    #print('theta_true =', G.theta_true)  
    
    x = x / N_simul
    y = y / N_simul
    z = z
    return (x, y, z)
        

       
if __name__ == "__main__":
    
    ## Set up model parameters
    K = 2       # number of arms
    T = 200      # time horizon
    #Npar = 100    # number of particles
    #T_epoch = 4  # Epoch time 
    N_simul = 1   # number of simulations
    
    #alg = 'TS'
    #Npar= 1000
    #(x1,y1,z1) = run_simulations(K,T,Npar,N_simul,alg)
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.61_to_0.70_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    #fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.5_to_0.7_' + alg + '_CUM', 'wb')
    #pickle.dump(x, fw)
    #fw.close()
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.61_to_0.70_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    #fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.5_to_0.7_' + alg + '_AVG', 'wb')
    #pickle.dump(y, fw)
    #fw.close()

    #alg = 'PR7'
    #Npar= 1000
    #(x2,y2) = run_simulations(K,T,Npar,N_simul,alg)
    #fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.5_to_0.7_' + alg + '_N' + str(Npar) + '_CUM', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.05_to_0.5_' + alg + '_T100K_CUM', 'wb')
    #pickle.dump(x, fw)
    #fw.close()
    #fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.5_to_0.7_' + alg + '_N' + str(Npar) + '_AVG', 'wb')
    ##fw = open('data/Bernoulli' + str(K) + '/Bernoulli' + str(K) + '_' + 'theta_0.05_to_0.5_' + alg + '_T100K_AVG', 'wb')
    #pickle.dump(y, fw)
    #fw.close()
 
    
    alg = 'PR8'
    Npar= 100
    (x2,y2,z2) = run_simulations(K,T,Npar,N_simul,alg)    
    
    
    #alg = 'PR7a'
    #Npar= 1000
    #(x3,y3) = run_simulations(K,T,Npar,N_simul,alg)     
    
    plt.figure(1)
    plt.plot(range(T), x1, color='red', linestyle='-', label = "TS")
    plt.plot(range(T), x2, color='blue', linestyle='-', label = "PR7-logt, Npar=1000")
    #plt.plot(range(T), x3, color='green', linestyle='-', label = "PR7a, Npar=1000")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('accumulative regret')
    #plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.30, \cdots, 0.80]$')
    #plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, \cdots, 0.60]$')
    plt.show()    
    
    plt.figure(2)
    plt.plot(range(T), y1, color='red', linestyle='-', label = "TS")
    plt.plot(range(T), y2, color='blue', linestyle='-', label = "PR7-logt, Npar=1000")
    #plt.plot(range(T), y3, color='green', linestyle='-', label = "PR7a, Npar=1000")
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('running average regret')
    #plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.30, \cdots, 0.80]$')
    #plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, \cdots, 0.60]$')
    plt.show()
    
    
    
    #gaps = [t - s for s, t in zip(z2, z2[1:])]
    #plt.figure(3)
    #plt.plot(range(len(gaps)), gaps, label = "PR4, Npar=1000")
    #plt.legend()
    #plt.grid()
    #plt.xlabel('number of epochs')
    #plt.ylabel('time gap between epochs')
    ##plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.30, \cdots, 0.80]$')
    #plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, \cdots, 0.60]$')
    #plt.show()    
   
    

    
       