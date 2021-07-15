import numpy as np
import matplotlib.pyplot as plt
import pickle


## 10-Arm Bernoulli, theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_TS_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_TS_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_TS_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_TS_T100K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR4_N100_T100K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR4_N100_T100K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR4_N100_T100K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR4_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR5_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR5_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR5_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR5_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR7_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR7_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR7_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR7_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR72_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR72_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR72_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR72_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR73_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR73_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR73_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR73_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR75_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR75_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR75_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR75_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR8_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR8_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR8_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR8_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N1000_T100K_AVG = pickle.load(fd)


#T = len(Bernoulli10_theta_051_to_060_TS_T100K_CUM)


#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_T100K_CUM, color='red', linestyle='-', label = "TS") 
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N1000_T100K_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N100_T100K_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N1000_T100K_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_T100K_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_T100K_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR72_N1000_T100K_CUM, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR73_N1000_T100K_CUM, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR75_N1000_T100K_CUM, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_T100K_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_T100K_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_T100K_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_T100K_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_T100K_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_T100K_AVG, color='red', linestyle='-', label = "TS") 
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N1000_T100K_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N100_T100K_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N1000_T100K_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_T100K_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_T100K_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR72_N1000_T100K_AVG, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR73_N1000_T100K_AVG, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR75_N1000_T100K_AVG, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_T100K_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_T100K_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_T100K_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_T100K_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_T100K_AVG.png')






# 100-Arm Bernoulli, theta^* = [0.3, ... , 0.8]

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_TS_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_TS_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_TS_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_TS_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PTS_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PTS_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR72_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR72_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR72_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR72_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR73_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR73_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR73_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR73_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR75_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR75_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR75_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR75_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7a_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7a_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7a_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7a_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7logt_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7logt_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7logt_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR7logt_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR8_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR8_N1000_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR9_N1000_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_03_to_08_PR9_N1000_AVG = pickle.load(fd)


T = len(Bernoulli100_theta_03_to_08_TS_CUM)


plt.figure(1)
plt.plot(range(T), Bernoulli100_theta_03_to_08_TS_CUM, color='red', linestyle='-', label = "TS") 
plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR72_N1000_CUM, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR73_N1000_CUM, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR75_N1000_CUM, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7a_N1000_CUM, color='green', linestyle='-', label = "PR7a, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7logt_N1000_CUM, color='fuchsia', linestyle='-', label = "PR7-logt, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('cumulative regret')
plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.3, \cdots, 0.8]$')
plt.ylim([0, 5000])
plt.show() 
plt.savefig('figs/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_CUM.png')


plt.figure(2)
plt.plot(range(T), Bernoulli100_theta_03_to_08_TS_AVG, color='red', linestyle='-', label = "TS") 
plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000") 
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR72_N1000_AVG, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR73_N1000_AVG, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR75_N1000_AVG, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7a_N1000_AVG, color='green', linestyle='-', label = "PR7a, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7logt_N1000_AVG, color='fuchsia', linestyle='-', label = "PR7-logt, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('running average regret')
plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.3, \cdots, 0.8]$')
plt.show() 
plt.savefig('figs/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_AVG.png')





## 100-Arm Bernoulli, theta^* = [0.5, ... , 0.7]

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR72_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR72_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR72_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR72_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR73_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR73_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR73_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR73_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR75_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR75_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR75_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR75_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N1000_AVG = pickle.load(fd)


#T = len(Bernoulli100_theta_05_to_07_TS_CUM)


#plt.figure(1)
#plt.plot(range(T), Bernoulli100_theta_05_to_07_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR72_N1000_CUM, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR73_N1000_CUM, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR75_N1000_CUM, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.ylim([0, 5000])
#plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.5, \cdots, 0.7]$')
#plt.show() 
#plt.savefig('figs/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli100_theta_05_to_07_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR72_N1000_AVG, color='silver', linestyle='-', label = "PR7-2, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR73_N1000_AVG, color='gold', linestyle='-', label = "PR7-3, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR75_N1000_AVG, color='lime', linestyle='-', label = "PR7-5, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('100-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.5, \cdots, 0.7]$')
#plt.show() 
#plt.savefig('figs/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_AVG.png')