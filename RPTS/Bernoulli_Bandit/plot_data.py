import numpy as np
import matplotlib.pyplot as plt
import pickle


## 2-Arm Bernoulli, theta*=[0.61, 0.62]

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_TS_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_TS_T200K_AVG = pickle.load(fd)


#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR4_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR4_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR4_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR4_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR5_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR5_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR5_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR5_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR72_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR72_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR72_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR72_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR73_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR73_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR73_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR73_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR75_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR75_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR75_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR75_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.61_0.62_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0612_PR9_N100_T200K_AVG = pickle.load(fd)

#T = len(Bernoulli2_theta0612_TS_T200K_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli2_theta0612_TS_T200K_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_theta0612_PTS_N100_T200K_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR4_N100_T200K_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR5_N100_T200K_CUM, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR7_N100_T200K_CUM, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR72_N100_T200K_CUM, color='silver', linestyle='-', label = "PR7-2, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR73_N100_T200K_CUM, color='gold', linestyle='-', label = "PR7-3, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR75_N100_T200K_CUM, color='lime', linestyle='-', label = "PR7-5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR8_N100_T200K_CUM, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR9_N100_T200K_CUM, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.61, 0.62]$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_theta_0.61_0.62_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli2_theta0612_TS_T200K_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_theta0612_PTS_N100_T200K_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR4_N100_T200K_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR5_N100_T200K_AVG, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR7_N100_T200K_AVG, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR72_N100_T200K_AVG, color='silver', linestyle='-', label = "PR7-2, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR73_N100_T200K_AVG, color='gold', linestyle='-', label = "PR7-3, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR75_N100_T200K_AVG, color='lime', linestyle='-', label = "PR7-5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR8_N100_T200K_AVG, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0612_PR9_N100_T200K_AVG, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.61, 0.62]$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_theta_0.61_0.62_AVG.png')





## 2-Arm Bernoulli, theta*=[0.6, 0.7]

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_TS_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_TS_T200K_AVG = pickle.load(fd)


#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR4_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR4_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR4_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR4_N100_T200K_AVG = pickle.load(fd)


#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR5_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR5_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR5_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR5_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_theta_0.6_0.7_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_theta0607_PR9_N100_T200K_AVG = pickle.load(fd)

#T = int(len(Bernoulli2_theta0607_TS_T200K_CUM)/2)

#plt.figure(1)
#plt.plot(range(T), Bernoulli2_theta0607_TS_T200K_CUM[:T], color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_theta0607_PTS_N100_T200K_CUM[:T], color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR4_N100_T200K_CUM[:T], color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR5_N100_T200K_CUM[:T], color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR7_N100_T200K_CUM[:T], color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR8_N100_T200K_CUM[:T], color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR9_N100_T200K_CUM[:T], color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.6, 0.7]$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_theta_0.6_0.7_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli2_theta0607_TS_T200K_AVG[:T], color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_theta0607_PTS_N100_T200K_AVG[:T], color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR4_N100_T200K_AVG[:T], color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR5_N100_T200K_AVG[:T], color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR7_N100_T200K_AVG[:T], color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR8_N100_T200K_AVG[:T], color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_theta0607_PR9_N100_T200K_AVG[:T], color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.6, 0.7]$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_theta_0.6_0.7_AVG.png')




## 2-Arm Bernoulli, random theta*

#inputFile = 'data/Bernoulli2/Bernoulli2_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PTS_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PTS_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PTS_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PTS_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR1_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR1_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR1_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR1_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR2_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR2_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR2_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR2_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR3_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR3_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR3_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR3_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR4_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR4_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR4_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR4_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR5_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR5_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR5_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR5_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR6_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR6_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR6_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR6_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR7_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR7_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR7_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR7_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR8_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR8_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR8_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR8_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR9_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR9_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR9_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR9_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli2/Bernoulli2_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli2_PR9_N100_AVG = pickle.load(fd)

#T = len(Bernoulli2_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli2_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_PTS_N10_CUM, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli2_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Bernoulli2_PR1_N10_CUM, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Bernoulli2_PR1_N100_CUM, color='blue', linestyle='-', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli2_PR2_N10_CUM, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Bernoulli2_PR2_N100_CUM, color='green', linestyle='-', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli2_PR3_N10_CUM, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Bernoulli2_PR3_N100_CUM, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli2_PR4_N10_CUM, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli2_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_PR5_N10_CUM, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Bernoulli2_PR5_N100_CUM, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_PR6_N10_CUM, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Bernoulli2_PR6_N100_CUM, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli2_PR7_N10_CUM, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Bernoulli2_PR7_N100_CUM, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_PR8_N10_CUM, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Bernoulli2_PR8_N100_CUM, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_PR9_N10_CUM, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Bernoulli2_PR9_N100_CUM, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli2_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli2_PTS_N10_AVG, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli2_PTS_N100_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Bernoulli2_PR1_N10_AVG, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Bernoulli2_PR1_N100_AVG, color='blue', linestyle='-', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli2_PR2_N10_AVG, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Bernoulli2_PR2_N100_AVG, color='green', linestyle='-', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli2_PR3_N10_AVG, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Bernoulli2_PR3_N100_AVG, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli2_PR4_N10_AVG, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli2_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli2_PR5_N10_AVG, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Bernoulli2_PR5_N100_AVG, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli2_PR6_N10_AVG, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Bernoulli2_PR6_N100_AVG, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli2_PR7_N10_AVG, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Bernoulli2_PR7_N100_AVG, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli2_PR8_N10_AVG, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Bernoulli2_PR8_N100_AVG, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli2_PR9_N10_AVG, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Bernoulli2_PR9_N100_AVG, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('2-Arm Bernoulli Bandit, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli2/Bernoulli2_AVG.png')





## 3-Arm Bernoulli, theta*=[0.1, 0.5, 0.8]

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PTS_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PTS_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PTS_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PTS_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR1_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR1_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR1_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR1_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR1_N100_AVG = pickle.load(fd)


#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR2_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR2_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR2_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR2_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR3_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR3_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR3_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR3_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR4_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR4_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR4_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR4_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta158_PR4_N100_AVG = pickle.load(fd)

#T = len(Bernoulli3_theta158_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli3_theta158_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_theta158_PTS_N10_CUM, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR1_N10_CUM, color='blue', linestyle='--', label = "PR1, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR1_N100_CUM, color='blue', linestyle='-', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR2_N10_CUM, color='green', linestyle='--', label = "PR2, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR2_N100_CUM, color='green', linestyle='-', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR3_N10_CUM, color='purple', linestyle='--', label = "PR3, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR3_N100_CUM, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR4_N10_CUM, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.1, 0.5, 0.8]$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli3_theta158_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_theta158_PTS_N10_AVG, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PTS_N100_AVG, color='orange', linestyle='-.', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR1_N10_AVG, color='blue', linestyle='--', label = "PR1, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR1_N100_AVG, color='blue', linestyle='-.', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR2_N10_AVG, color='green', linestyle='--', label = "PR2, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR2_N100_AVG, color='green', linestyle='-.', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR3_N10_AVG, color='purple', linestyle='--', label = "PR3, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR3_N100_AVG, color='purple', linestyle='-.', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_theta158_PR4_N10_AVG, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_theta158_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.1, 0.5, 0.8]$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_theta_0.1_0.5_0.8_AVG.png')




## 3-Arm Bernoulli, theta*=[0.1, 0.3, 0.5]

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PTS_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PTS_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PTS_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PTS_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PTS_N100_AVG = pickle.load(fd)


#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR1_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR1_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR1_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR1_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR2_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR2_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR2_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR2_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR3_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR3_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR3_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR3_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR4_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR4_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR4_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR4_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_theta135_PR4_N100_AVG = pickle.load(fd)

#T = len(Bernoulli3_theta135_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli3_theta135_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_theta135_PTS_N10_CUM, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR1_N10_CUM, color='blue', linestyle='--', label = "PR1, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR1_N100_CUM, color='blue', linestyle='-', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR2_N10_CUM, color='green', linestyle='--', label = "PR2, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR2_N100_CUM, color='green', linestyle='-', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR3_N10_CUM, color='purple', linestyle='--', label = "PR3, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR3_N100_CUM, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR4_N10_CUM, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.1, 0.3, 0.5]$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli3_theta135_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_theta135_PTS_N10_AVG, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PTS_N100_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR1_N10_AVG, color='blue', linestyle='--', label = "PR1, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR1_N100_AVG, color='blue', linestyle='-', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR2_N10_AVG, color='green', linestyle='--', label = "PR2, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR2_N100_AVG, color='green', linestyle='-', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR3_N10_AVG, color='purple', linestyle='--', label = "PR3, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR3_N100_AVG, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_theta135_PR4_N10_AVG, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_theta135_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'$\theta^* = [0.1, 0.3, 0.5]$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_theta_0.1_0.3_0.5_AVG.png')



## 3-Arm Bernoulli, random initialized theta^*

#inputFile = 'data/Bernoulli3/Bernoulli3_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PTS_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PTS_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PTS_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PTS_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR1_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR1_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR1_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR1_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR2_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR2_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR2_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR2_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR3_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR3_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR3_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR3_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR4_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR4_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR4_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR4_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR5_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR5_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR5_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR5_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR6_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR6_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR6_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR6_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR7_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR7_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR7_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR7_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR8_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR8_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR8_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR8_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR9_N10_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR9_N10_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR9_N10_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR9_N10_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli3/Bernoulli3_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli3_PR9_N100_AVG = pickle.load(fd)

#T = len(Bernoulli3_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli3_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_PTS_N10_CUM, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_PTS_N100_CUM, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Bernoulli3_PR1_N10_CUM, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Bernoulli3_PR1_N100_CUM, color='blue', linestyle='-', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli3_PR2_N10_CUM, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Bernoulli3_PR2_N100_CUM, color='green', linestyle='-', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli3_PR3_N10_CUM, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Bernoulli3_PR3_N100_CUM, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_PR4_N10_CUM, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_PR4_N100_CUM, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli3_PR5_N10_CUM, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Bernoulli3_PR5_N100_CUM, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli3_PR6_N10_CUM, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Bernoulli3_PR6_N100_CUM, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli3_PR7_N10_CUM, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Bernoulli3_PR7_N100_CUM, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli3_PR8_N10_CUM, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Bernoulli3_PR8_N100_CUM, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli3_PR9_N10_CUM, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Bernoulli3_PR9_N100_CUM, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli3_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli3_PTS_N10_AVG, color='orange', linestyle='--', label = "PTS, Npar=10")
#plt.plot(range(T), Bernoulli3_PTS_N100_AVG, color='orange', linestyle='-', label = "PTS, Npar=100")
##plt.plot(range(T), Bernoulli3_PR1_N10_AVG, color='blue', linestyle='--', label = "PR1, Npar=10")
##plt.plot(range(T), Bernoulli3_PR1_N100_AVG, color='blue', linestyle='-', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli3_PR2_N10_AVG, color='green', linestyle='--', label = "PR2, Npar=10")
##plt.plot(range(T), Bernoulli3_PR2_N100_AVG, color='green', linestyle='-', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli3_PR3_N10_AVG, color='purple', linestyle='--', label = "PR3, Npar=10")
##plt.plot(range(T), Bernoulli3_PR3_N100_AVG, color='purple', linestyle='-', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli3_PR4_N10_AVG, color='cyan', linestyle='--', label = "PR4, Npar=10")
#plt.plot(range(T), Bernoulli3_PR4_N100_AVG, color='cyan', linestyle='-', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli3_PR5_N10_AVG, color='blue', linestyle='--', label = "PR5, Npar=10")
#plt.plot(range(T), Bernoulli3_PR5_N100_AVG, color='blue', linestyle='-', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli3_PR6_N10_AVG, color='green', linestyle='--', label = "PR6, Npar=10")
#plt.plot(range(T), Bernoulli3_PR6_N100_AVG, color='green', linestyle='-', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli3_PR7_N10_AVG, color='purple', linestyle='--', label = "PR7, Npar=10")
#plt.plot(range(T), Bernoulli3_PR7_N100_AVG, color='purple', linestyle='-', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli3_PR8_N10_AVG, color='brown', linestyle='--', label = "PR8, Npar=10")
#plt.plot(range(T), Bernoulli3_PR8_N100_AVG, color='brown', linestyle='-', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli3_PR9_N10_AVG, color='black', linestyle='--', label = "PR9, Npar=10")
#plt.plot(range(T), Bernoulli3_PR9_N100_AVG, color='black', linestyle='-', label = "PR9, Npar=100")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('3-Arm Bernoulli Bandit, ' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli3/Bernoulli3_AVG.png')




## 10-Arm Bernoulli, theta^* = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR1_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR1_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR1_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR1_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR2_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR2_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR2_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR2_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR3_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR3_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR3_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR3_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_05_to_95_PR4_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_05_to_95_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_05_to_95_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N10000_CUM, color='orange', linestyle='-', label = "PTS, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N100_CUM, color='blue', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N1000_CUM, color='blue', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N10000_CUM, color='blue', linestyle='-', label = "PR1, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N100_CUM, color='green', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N1000_CUM, color='green', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N10000_CUM, color='green', linestyle='-', label = "PR2, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N100_CUM, color='purple', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N1000_CUM, color='purple', linestyle='-', label = "PR3, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N10000_CUM, color='purple', linestyle='-', label = "PR3, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_05_to_95_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PTS_N10000_AVG, color='orange', linestyle='-', label = "PTS, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N100_AVG, color='blue', linestyle='--', label = "PR1, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N1000_AVG, color='blue', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR1_N10000_AVG, color='blue', linestyle='-', label = "PR1, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N100_AVG, color='green', linestyle='--', label = "PR2, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N1000_AVG, color='green', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR2_N10000_AVG, color='green', linestyle='-', label = "PR2, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N100_AVG, color='purple', linestyle='--', label = "PR3, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N1000_AVG, color='purple', linestyle='-', label = "PR3, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_05_to_95_PR3_N10000_AVG, color='purple', linestyle='-', label = "PR3, Npar=10000")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_05_to_95_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.05_to_0.95_AVG.png')



## 10-Arm Bernoulli, theta^* = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR1_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR1_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR1_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR1_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR2_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR2_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR2_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR2_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR3_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR3_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR3_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR3_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_05_PR9_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_005_to_05_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_005_to_05_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR1_N100_CUM, color='gold', linestyle='--', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR1_N1000_CUM, color='gold', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR2_N100_CUM, color='silver', linestyle='--', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR2_N1000_CUM, color='silver', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR3_N100_CUM, color='lime', linestyle='--', label = "PR3, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR3_N1000_CUM, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_005_to_05_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR1_N100_AVG, color='gold', linestyle='--', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR1_N1000_AVG, color='gold', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR2_N100_AVG, color='silver', linestyle='--', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR2_N1000_AVG, color='silver', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR3_N100_AVG, color='lime', linestyle='--', label = "PR3, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR3_N1000_AVG, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_005_to_05_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_005_to_05_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_AVG.png')



## 10-Arm Bernoulli, theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR1_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR1_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR1_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR1_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR1_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR1_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR1_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR1_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR2_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR2_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR2_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR2_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR2_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR2_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR2_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR2_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR3_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR3_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR3_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR3_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR3_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR3_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR3_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR3_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PR9_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_051_to_060_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR1_N100_CUM, color='gold', linestyle='--', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR1_N1000_CUM, color='gold', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR2_N100_CUM, color='silver', linestyle='--', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR2_N1000_CUM, color='silver', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR3_N100_CUM, color='lime', linestyle='--', label = "PR3, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR3_N1000_CUM, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR1_N100_AVG, color='gold', linestyle='--', label = "PR1, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR1_N1000_AVG, color='gold', linestyle='-', label = "PR1, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR2_N100_AVG, color='silver', linestyle='--', label = "PR2, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR2_N1000_AVG, color='silver', linestyle='-', label = "PR2, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR3_N100_AVG, color='lime', linestyle='--', label = "PR3, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR3_N1000_AVG, color='lime', linestyle='-', label = "PR3, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_theta_0.51_to_0.60_AVG.png')




## 10-Arm Bernoulli, theta^* = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70]

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.61_to_0.70_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_061_to_070_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.61_to_0.70_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_061_to_070_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.61_to_0.70_RBMLE_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_061_to_070_RBMLE_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.61_to_0.70_RBMLE_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_061_to_070_RBMLE_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_061_to_070_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_061_to_070_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_061_to_070_RBMLE_CUM, color='blue', linestyle='-', label = "RBMLE") 
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/RBMLE/Bernoulli10_theta_0.61_to_0.70_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_061_to_070_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_061_to_070_RBMLE_AVG, color='blue', linestyle='-', label = "RBMLE") 
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/RBMLE/Bernoulli10_theta_0.61_to_0.70_AVG.png')



## 10-Arm Bernoulli, theta^* = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50], T=100K

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_TS_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_TS_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_TS_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_TS_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_RBMLE_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_RBMLE_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_theta_0.05_to_0.5_RBMLE_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_RBMLE_T100K_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_005_to_050_TS_T100K_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_theta_005_to_050_TS_T100K_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_005_to_050_RBMLE_T100K_CUM, color='blue', linestyle='-', label = "RBMLE") 
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/RBMLE/Bernoulli10_theta_0.05_to_0.5_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_theta_005_to_050_TS_T100K_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_theta_005_to_050_RBMLE_T100K_AVG, color='blue', linestyle='-', label = "RBMLE") 
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'$\theta^* = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/RBMLE/Bernoulli10_theta_0.05_to_0.5_AVG.png')


## 10-Arm Bernoulli, randomly initialize theta*

#inputFile = 'data/Bernoulli10/Bernoulli10_TS_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_TS_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_TS_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_TS_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PTS_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PTS_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PTS_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PTS_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PTS_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PTS_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PTS_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PTS_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR4_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR4_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR4_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR4_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR4_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR4_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR4_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR4_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR5_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR5_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR5_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR5_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR5_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR5_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR5_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR5_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR6_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR6_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR6_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR6_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR6_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR6_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR6_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR6_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR7_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR7_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR7_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR7_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR7_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR7_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR7_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR7_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR8_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR8_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR8_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR8_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR8_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR8_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR8_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR8_N1000_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR9_N100_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR9_N100_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR9_N100_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR9_N100_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR9_N1000_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR9_N1000_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10/Bernoulli10_PR9_N1000_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_PR9_N1000_AVG = pickle.load(fd)

#T = len(Bernoulli10_TS_CUM)

#plt.figure(1)
#plt.plot(range(T), Bernoulli10_TS_CUM, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_PTS_N100_CUM, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_PTS_N1000_CUM, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR4_N100_CUM, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_PR4_N1000_CUM, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR5_N100_CUM, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_PR5_N1000_CUM, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR6_N100_CUM, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_PR6_N1000_CUM, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR7_N100_CUM, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_PR7_N1000_CUM, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR8_N100_CUM, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_PR8_N1000_CUM, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR9_N100_CUM, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_PR9_N1000_CUM, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('cumulative regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_CUM.png')


#plt.figure(2)
#plt.plot(range(T), Bernoulli10_TS_AVG, color='red', linestyle='-', label = "TS") 
#plt.plot(range(T), Bernoulli10_PTS_N100_AVG, color='orange', linestyle='--', label = "PTS, Npar=100")
#plt.plot(range(T), Bernoulli10_PTS_N1000_AVG, color='orange', linestyle='-', label = "PTS, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR4_N100_AVG, color='cyan', linestyle='--', label = "PR4, Npar=100")
#plt.plot(range(T), Bernoulli10_PR4_N1000_AVG, color='cyan', linestyle='-', label = "PR4, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR5_N100_AVG, color='blue', linestyle='--', label = "PR5, Npar=100")
#plt.plot(range(T), Bernoulli10_PR5_N1000_AVG, color='blue', linestyle='-', label = "PR5, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR6_N100_AVG, color='green', linestyle='--', label = "PR6, Npar=100")
#plt.plot(range(T), Bernoulli10_PR6_N1000_AVG, color='green', linestyle='-', label = "PR6, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR7_N100_AVG, color='purple', linestyle='--', label = "PR7, Npar=100")
#plt.plot(range(T), Bernoulli10_PR7_N1000_AVG, color='purple', linestyle='-', label = "PR7, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR8_N100_AVG, color='brown', linestyle='--', label = "PR8, Npar=100")
#plt.plot(range(T), Bernoulli10_PR8_N1000_AVG, color='brown', linestyle='-', label = "PR8, Npar=1000")
#plt.plot(range(T), Bernoulli10_PR9_N100_AVG, color='black', linestyle='--', label = "PR9, Npar=100")
#plt.plot(range(T), Bernoulli10_PR9_N1000_AVG, color='black', linestyle='-', label = "PR9, Npar=1000")
#plt.legend()
#plt.grid()
#plt.xlabel('t')
#plt.ylabel('running average regret')
#plt.title('10-Arm Bernoulli Bandit \n' + r'randomly initialized $\theta^*$')
#plt.show() 
#plt.savefig('figs/Bernoulli10/Bernoulli10_AVG.png')