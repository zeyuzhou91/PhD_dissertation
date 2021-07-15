import numpy as np
import matplotlib.pyplot as plt
import pickle

## K=5, M=2

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PTS_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PTS_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PTS_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PTS_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR4_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR4_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR4_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR4_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR5_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR5_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR5_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR5_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR6_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR6_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR6_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR6_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR7_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR7_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR7_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR7_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR8_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR8_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR8_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR8_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR9_N20_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR9_N20_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR9_N20_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR9_N20_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli5_Max2/Bernoulli5_Max2_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli5_Max2_PR9_N100_AVG = pickle.load(fd)

#T = len(Bernoulli5_Max2_PTS_N100_CUM)

#plt.figure(1) 
#plt.plot(range(T), Bernoulli5_Max2_PTS_N20_CUM, color='orange', linestyle='--', label = "PTS, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR4_N20_CUM, color='cyan', linestyle='--', label = "PR4, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR5_N20_CUM, color='blue', linestyle='--', label = "PR5, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR5_N100_CUM, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR6_N20_CUM, color='green', linestyle='--', label = "PR6, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR6_N100_CUM, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR7_N20_CUM, color='purple', linestyle='--', label = "PR7, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR7_N100_CUM, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR8_N20_CUM, color='brown', linestyle='--', label = "PR8, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR8_N100_CUM, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR9_N20_CUM, color='black', linestyle='--', label = "PR9, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR9_N100_CUM, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('5-Arm Bernoulli Bandit, Choose 2, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli5_Max2/Bernoulli5_Max2_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli5_Max2_PTS_N20_AVG, color='orange', linestyle='--', label = "PTS, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PTS_N100_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR4_N20_AVG, color='cyan', linestyle='--', label = "PR4, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR5_N20_AVG, color='blue', linestyle='--', label = "PR5, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR5_N100_AVG, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR6_N20_AVG, color='green', linestyle='--', label = "PR6, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR6_N100_AVG, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR7_N20_AVG, color='purple', linestyle='--', label = "PR7, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR7_N100_AVG, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR8_N20_AVG, color='brown', linestyle='--', label = "PR8, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR8_N100_AVG, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli5_Max2_PR9_N20_AVG, color='black', linestyle='--', label = "PR9, Npar=20")
#plt.plot(range(T), Bernoulli5_Max2_PR9_N100_AVG, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('5-Arm Bernoulli Bandit, Choose 2, '+ r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli5_Max2/Bernoulli5_Max2_AVG.png')





## K=10, M=3

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_PR9_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_Max3_PTS_N100_CUM)

#plt.figure(1) 
#plt.plot(range(T), Bernoulli10_Max3_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_Max3_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_AVG.png')



## K=10, M=3, theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR1_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR1_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR1_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR1_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR2_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR2_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR2_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR2_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR3_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR3_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR3_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR3_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_Max3_theta_051_to_060_PR4_N100_CUM)

#plt.figure(1) 
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR1_N100_CUM, color='gold', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR1_N1000_CUM, color='gold', linestyle='-', label = "PR1, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR2_N100_CUM, color='silver', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR2_N1000_CUM, color='silver', linestyle='-', label = "PR2, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR3_N100_CUM, color='lime', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR3_N1000_CUM, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3 \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_theta_051_to_060_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR1_N100_AVG, color='gold', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR1_N1000_AVG, color='gold', linestyle='-', label = "PR1, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR2_N100_AVG, color='silver', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR2_N1000_AVG, color='silver', linestyle='-', label = "PR2, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR3_N100_AVG, color='lime', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR3_N1000_AVG, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3 \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_theta_051_to_060_AVG.png')



## K=10, M=3, theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60], T=200K

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PTS_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR4_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR4_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR5_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR5_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR7_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR7_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR8_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR8_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_Max3/Bernoulli10_Max3_theta_0.51_to_0.60_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_051_to_060_PR9_N1000_T200K_AVG = pickle.load(fd)

#T = len(Bernoulli10_Max3_theta_051_to_060_PR4_N100_T200K_CUM)

#plt.figure(1) 
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N100_T200K_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N1000_T200K_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N100_T200K_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N1000_T200K_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N100_T200K_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N1000_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N100_T200K_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N1000_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N100_T200K_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N1000_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3 \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_theta_051_to_060_T200K_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N100_T200K_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR4_N1000_T200K_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N100_T200K_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR5_N1000_T200K_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N100_T200K_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR7_N1000_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N100_T200K_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR8_N1000_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N100_T200K_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_Max3_theta_051_to_060_PR9_N1000_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit, Choose 3 \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10_Max3/Bernoulli10_Max3_theta_051_to_060_T200K_AVG.png')





## K=100, M=5, theta^* = [0.3, ... , 0.8], T=200K

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PTS_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PTS_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PTS_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PTS_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR7_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR7_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR7_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR7_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR8_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR8_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR8_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR8_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR9_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.3_to_0.8_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_Max3_theta_03_to_08_PR9_N1000_T200K_AVG = pickle.load(fd)


#T = len(Bernoulli10_Max3_theta_03_to_08_PTS_N1000_T200K_CUM)

#plt.figure(1) 
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR7_N1000_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR8_N1000_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR9_N1000_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('100-Arm Bernoulli Bandit, Choose 5 \n' + r'$\theta^* = [0.3, ... , 0.8]$')
#plt.show() 
#plt.savefig('figs/Bernoulli100_Max5/Bernoulli100_Max5_theta_03_to_08_T200K_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR7_N1000_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR8_N1000_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_Max3_theta_03_to_08_PR9_N1000_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('100-Arm Bernoulli Bandit, Choose 5 \n' + r'$\theta^* = [0.3, ... , 0.8]$')
#plt.show() 
#plt.savefig('figs/Bernoulli100_Max5/Bernoulli100_Max5_theta_03_to_08_T200K_AVG.png')



# K=100, M=5, theta^* = [0.5, ... , 0.7], T=200K

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PTS_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PTS_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PTS_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PTS_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR7_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR7_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR7_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR7_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR8_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR8_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR8_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR8_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR9_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR9_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100_Max5/Bernoulli100_Max5_theta_0.5_to_0.7_PR9_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli10_Max3_theta_05_to_07_PR9_N1000_T200K_AVG = pickle.load(fd)


T = len(Bernoulli10_Max3_theta_05_to_07_PTS_N1000_T200K_CUM)

plt.figure(1) 
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR7_N1000_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR8_N1000_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR9_N1000_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('cumulative regret')
plt.title('100-Arm Bernoulli Bandit, Choose 5 \n' + r'$\theta^* = [0.5, ... , 0.7]$')
plt.show() 
plt.savefig('figs/Bernoulli100_Max5/Bernoulli100_Max5_theta_05_to_07_T200K_CUM.png')


plt.figure(2)
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR7_N1000_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR8_N1000_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Bernoulli10_Max3_theta_05_to_07_PR9_N1000_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('running average regret')
plt.title('100-Arm Bernoulli Bandit, Choose 5 \n' + r'$\theta^* = [0.5, ... , 0.7]$')
plt.show() 
plt.savefig('figs/Bernoulli100_Max5/Bernoulli100_Max5_theta_05_to_07_T200K_AVG.png')