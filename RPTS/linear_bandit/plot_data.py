import numpy as np
import matplotlib.pyplot as plt
import pickle

## Linear bandit, Dimension 2, var_W=0.1, randomly initialized theta*

#inputFile = 'data/D2/Linear_D2_TS_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_TS_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_TS_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_TS_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PTS_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PTS_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PTS_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PTS_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR4_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR4_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR4_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR4_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR5_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR5_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR5_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR5_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR6_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR6_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR6_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR6_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR7_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR7_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR7_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR7_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR8_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR8_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR8_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR8_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR9_N10_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR9_N10_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR9_N10_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR9_N10_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_PR9_N100_AVG = pickle.load(fd)

#T = len(Linear_D2_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Linear_D2_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D2_PTS_N10_CUM, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Linear_D2_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Linear_D2_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Linear_D2_PR1_N10_CUM, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Linear_D2_PR1_N100_CUM, color='blue', linestyle='-', label = "PR1, Npar=100")
###plt.plot(range(T), Linear_D2_PR1_N1000_CUM, color='blue', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Linear_D2_PR2_N10_CUM, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Linear_D2_PR2_N100_CUM, color='green', linestyle='-', label = "PR2, Npar=100")
###plt.plot(range(T), Linear_D2_PR2_N1000_CUM, color='green', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Linear_D2_PR3_N10_CUM, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Linear_D2_PR3_N100_CUM, color='purple', linestyle='-', label = "PR3, Npar=100")
###plt.plot(range(T), Linear_D2_PR3_N1000_CUM, color='purple', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Linear_D2_PR4_N10_CUM, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Linear_D2_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
##plt.plot(range(T), Linear_D2_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D2_PR5_N10_CUM, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Linear_D2_PR5_N100_CUM, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D2_PR6_N10_CUM, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Linear_D2_PR6_N100_CUM, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Linear_D2_PR7_N10_CUM, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Linear_D2_PR7_N100_CUM, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D2_PR8_N10_CUM, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Linear_D2_PR8_N100_CUM, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D2_PR9_N10_CUM, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Linear_D2_PR9_N100_CUM, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('2-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/D2/Linear_D2_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Linear_D2_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D2_PTS_N10_AVG, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Linear_D2_PTS_N100_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Linear_D2_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Linear_D2_PR1_N10_AVG, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Linear_D2_PR1_N100_AVG, color='blue', linestyle='-', label = "PR1, Npar=100")
###plt.plot(range(T), Linear_D2_PR1_N1000_AVG, color='blue', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Linear_D2_PR2_N10_AVG, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Linear_D2_PR2_N100_AVG, color='green', linestyle='-', label = "PR2, Npar=100")
###plt.plot(range(T), Linear_D2_PR2_N1000_AVG, color='green', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Linear_D2_PR3_N10_AVG, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Linear_D2_PR3_N100_AVG, color='purple', linestyle='-', label = "PR3, Npar=100")
###plt.plot(range(T), Linear_D2_PR3_N1000_AVG, color='purple', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Linear_D2_PR4_N10_AVG, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Linear_D2_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
##plt.plot(range(T), Linear_D2_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D2_PR5_N10_AVG, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Linear_D2_PR5_N100_AVG, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D2_PR6_N10_AVG, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Linear_D2_PR6_N100_AVG, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Linear_D2_PR7_N10_AVG, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Linear_D2_PR7_N100_AVG, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D2_PR8_N10_AVG, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Linear_D2_PR8_N100_AVG, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D2_PR9_N10_AVG, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Linear_D2_PR9_N100_AVG, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('2-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/D2/Linear_D2_AVG.png')




## Linear bandit, Dimension 2, var_W=0.1, theta* = [0.5, 0.5]

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_TS_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_TS_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR9_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR5_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR5_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR5_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR5_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR4_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR4_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D2/Linear_D2_theta_0.5x2_PR4_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D2_theta_05x2_PR4_N100_T200K_AVG = pickle.load(fd)


#T = int(len(Linear_D2_theta_05x2_TS_T200K_CUM)/10)

#plt.figure(1)
#plt.plot(range(T), Linear_D2_theta_05x2_TS_T200K_CUM[:T], color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D2_theta_05x2_PTS_N100_T200K_CUM[:T], color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR4_N100_T200K_CUM[:T], color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR5_N100_T200K_CUM[:T], color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR7_N100_T200K_CUM[:T], color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR8_N100_T200K_CUM[:T], color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR9_N100_T200K_CUM[:T], color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('2-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.5, 0.5]$')
#plt.show() 
#plt.savefig('figs/D2/Linear_D2_theta_0.5x2_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Linear_D2_theta_05x2_TS_T200K_AVG[:T], color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D2_theta_05x2_PTS_N100_T200K_AVG[:T], color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR4_N100_T200K_AVG[:T], color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR5_N100_T200K_AVG[:T], color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR7_N100_T200K_AVG[:T], color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR8_N100_T200K_AVG[:T], color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D2_theta_05x2_PR9_N100_T200K_AVG[:T], color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('2-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.5, 0.5]$')
#plt.show() 
#plt.savefig('figs/D2/Linear_D2_theta_0.5x2_AVG.png')




## Linear bandit, Dimension 10, var_W=0.1, randomly initialized theta*

#inputFile = 'data/D10/Linear_D10_TS_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_TS_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_TS_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_TS_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR1_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR1_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR1_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR1_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR2_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR2_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR2_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR2_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR3_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR3_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR3_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR3_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_PR9_N1000_AVG = pickle.load(fd)

#T = len(Linear_D10_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Linear_D10_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D10_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D10_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Linear_D10_PR1_N100_CUM, color='gold', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Linear_D10_PR1_N1000_CUM, color='gold', linestyle='-', label = "PR1, Npar=1000")
#plt.plot(range(T), Linear_D10_PR2_N100_CUM, color='silver', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Linear_D10_PR2_N1000_CUM, color='silver', linestyle='-', label = "PR2, Npar=1000")
#plt.plot(range(T), Linear_D10_PR3_N100_CUM, color='lime', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Linear_D10_PR3_N1000_CUM, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Linear_D10_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D10_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D10_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D10_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Linear_D10_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Linear_D10_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Linear_D10_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D10_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Linear_D10_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D10_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Linear_D10_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Linear_D10_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/D10/Linear_D10_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Linear_D10_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D10_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D10_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Linear_D10_PR1_N100_AVG, color='gold', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Linear_D10_PR1_N1000_AVG, color='gold', linestyle='-', label = "PR1, Npar=1000")
#plt.plot(range(T), Linear_D10_PR2_N100_AVG, color='silver', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Linear_D10_PR2_N1000_AVG, color='silver', linestyle='-', label = "PR2, Npar=1000")
#plt.plot(range(T), Linear_D10_PR3_N100_AVG, color='lime', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Linear_D10_PR3_N1000_AVG, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Linear_D10_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D10_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D10_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D10_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Linear_D10_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Linear_D10_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Linear_D10_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D10_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Linear_D10_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D10_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Linear_D10_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Linear_D10_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/D10/Linear_D10_AVG.png')




## Linear bandit, Dimension 10, var_W=0.1, theta* = [0.2, ..., 0.2]

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_TS_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_TS_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PTS_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PTS_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PTS_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PTS_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR4_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR4_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR4_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR4_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR4_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR4_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR4_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR4_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR5_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR5_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR5_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR5_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR5_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR5_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR5_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR5_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR7_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR7_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR7_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR7_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR8_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR8_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR8_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR8_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR9_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR9_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D10_theta_02x10_PR9_N1000_T200K_AVG = pickle.load(fd)

#T = len(Linear_D10_theta_02x10_TS_T200K_CUM)

#plt.figure(1)
#plt.plot(range(T), Linear_D10_theta_02x10_TS_T200K_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR4_N100_T200K_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR4_N1000_T200K_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR5_N100_T200K_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR5_N1000_T200K_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N100_T200K_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N1000_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N100_T200K_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N1000_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR9_N100_T200K_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR9_N1000_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.ylim([0,10000])
#plt.title('10-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.2, ..., 0.2]$')
#plt.show() 
#plt.savefig('figs/D10/Linear_D10_theta_0.2x10_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Linear_D10_theta_02x10_TS_T200K_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR4_N100_T200K_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR4_N1000_T200K_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR5_N100_T200K_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR5_N1000_T200K_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N100_T200K_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N1000_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N100_T200K_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N1000_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Linear_D10_theta_02x10_PR9_N100_T200K_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Linear_D10_theta_02x10_PR9_N1000_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.2, ..., 0.2]$')
#plt.show() 
#plt.savefig('figs/D10/Linear_D10_theta_0.2x10_AVG.png')




# Linear bandit, Dimension 100, var_W=0.1, theta* = [0.08, ..., 0.08]

inputFile = 'data/D100/Linear_D100_theta_0.08x100_TS_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_TS_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_TS_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_TS_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR9_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR9_N1000_T200K_AVG = pickle.load(fd)

T = len(Linear_D100_theta_008x100_TS_T200K_CUM)

plt.figure(1)
plt.plot(range(T), Linear_D100_theta_008x100_TS_T200K_CUM, color='red', linestyle='-', label = "TS") 
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N1000_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N1000_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR9_N1000_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('cumulative regret')
#plt.ylim([0,10000])
plt.title('100-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.08, ..., 0.08]$')
plt.show() 
plt.savefig('figs/D100/Linear_D100_theta_0.08x100_CUM.png')


plt.figure(2)
plt.plot(range(T), Linear_D100_theta_008x100_TS_T200K_AVG, color='red', linestyle='-', label = "TS") 
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N1000_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N1000_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Linear_D100_theta_008x100_PR9_N1000_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('running average regret')
plt.title('100-Dimensional Linear bandit, ' + r'$\sigma^2_W=0.1$, ' + r'$\theta^* = [0.08, ..., 0.08]$')
plt.show() 
plt.savefig('figs/D100/Linear_D100_theta_0.08x100_AVG.png')

