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

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PTS_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PTS_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PTS_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PTS_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_051_to_060_PTS_N1000_T100K_AVG = pickle.load(fd)

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

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N100_T100K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR9_N100_T100K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N100_T100K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR9_N100_T100K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_T100K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR9_N1000_T100K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.51_to_0.60_PR9_N1000_T100K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_051_to_060_PR9_N1000_T100K_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_051_to_060_TS_T100K_CUM)
#label_fs = 14

##plt.figure(1)
#plt.figure(1, figsize=(8, 6))
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N100_T100K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N1000_T100K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_T100K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_T100K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_T100K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_T100K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_T100K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_T100K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_T100K_CUM, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('cumulative regret', fontsize=label_fs)
#plt.ylim([0, 2000])
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli10_theta_0.51_to_0.60_CUM.png')


##plt.figure(2)
#plt.figure(2, figsize=(8, 6))
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N100_T100K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PTS_N1000_T100K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N100_T100K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR7_N1000_T100K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N100_T100K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_PR8_N1000_T100K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N100_T100K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli10_theta_051_to_060_PR9_N1000_T100K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_051_to_060_TS_T100K_AVG, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('running average regret', fontsize=label_fs)
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli10_theta_0.51_to_0.60_AVG.png')






## 10-Arm Bernoulli, theta^* = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_TS_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_TS_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_TS_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_TS_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PTS_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PTS_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PTS_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PTS_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PTS_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PTS_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PTS_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PTS_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR7_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR7_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR7_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR7_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR7_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR7_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR7_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR7_N1000_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR8_N100_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR8_N100_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR8_N100_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR8_N100_T100K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR8_N1000_T100K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR8_N1000_T100K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR8_N1000_T100K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli10_theta_005_to_050_PR8_N1000_T100K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR9_N100_T100K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_005_to_050_PR9_N100_T100K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR9_N100_T100K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_005_to_050_PR9_N100_T100K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR9_N1000_T100K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_005_to_050_PR9_N1000_T100K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli10_T100K/Bernoulli10_theta_0.05_to_0.50_PR9_N1000_T100K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli10_theta_005_to_050_PR9_N1000_T100K_AVG = pickle.load(fd)

#T = len(Bernoulli10_theta_005_to_050_TS_T100K_CUM)
#label_fs = 14

##plt.figure(1)
#plt.figure(1, figsize=(8, 6))
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PTS_N100_T100K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PTS_N1000_T100K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR7_N100_T100K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR7_N1000_T100K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR8_N100_T100K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR8_N1000_T100K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli10_theta_005_to_050_PR9_N100_T100K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli10_theta_005_to_050_PR9_N1000_T100K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_TS_T100K_CUM, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('cumulative regret', fontsize=label_fs)
#plt.ylim([0, 2000])
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli10_theta_0.05_to_0.50_CUM.png')


##plt.figure(2)
#plt.figure(2, figsize=(8, 6))
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PTS_N100_T100K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PTS_N1000_T100K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR7_N100_T100K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR7_N1000_T100K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR8_N100_T100K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_PR8_N1000_T100K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli10_theta_005_to_050_PR9_N100_T100K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli10_theta_005_to_050_PR9_N1000_T100K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli10_theta_005_to_050_TS_T100K_AVG, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('running average regret', fontsize=label_fs)
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli10_theta_0.05_to_0.50_AVG.png')






## 100-Arm Bernoulli, theta^* = [0.3, ... , 0.8]

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_TS_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_TS_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_TS_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_TS_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PTS_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PTS_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PTS_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PTS_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PTS_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR7_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR7_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR7_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR7_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR7_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR8_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR8_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR8_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR8_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_03_to_08_PR8_N1000_T200K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N100_T200K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli100_theta_03_to_08_PR9_N100_T200K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N100_T200K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli100_theta_03_to_08_PR9_N100_T200K_AVG = pickle.load(fd)

##inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N1000_T200K_CUM'
##fd = open(inputFile, 'rb')
##Bernoulli100_theta_03_to_08_PR9_N1000_T200K_CUM = pickle.load(fd)

##inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.3_to_0.8_PR9_N1000_T200K_AVG'
##fd = open(inputFile, 'rb')
##Bernoulli100_theta_03_to_08_PR9_N1000_T200K_AVG = pickle.load(fd)

#T = len(Bernoulli100_theta_03_to_08_TS_T200K_CUM)
#label_fs = 14

##plt.figure(1)
#plt.figure(1, figsize=(8, 6))
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N100_T200K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N1000_T200K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N100_T200K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N1000_T200K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N100_T200K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N1000_T200K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_TS_T200K_CUM, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.xlim([-5000, 100000])
#plt.ylabel('cumulative regret', fontsize=label_fs)
#plt.ylim([0, 4000])
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli100_theta_0.3_to_0.8_CUM.png')


##plt.figure(2)
#plt.figure(2, figsize=(8, 6))
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N100_T200K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR7_N1000_T200K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N100_T200K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_PR8_N1000_T200K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N100_T200K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Bernoulli100_theta_03_to_08_PR9_N1000_T200K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_03_to_08_TS_T200K_AVG, color='red', linestyle='-', label = "TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.xlim([-5000, 100000])
#plt.ylabel('running average regret', fontsize=label_fs)
#plt.show() 
#plt.savefig('figs_thesis/Bernoulli100_theta_0.3_to_0.8_AVG.png')




# 100-Arm Bernoulli, theta^* = [0.5, ... , 0.7]

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_TS_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_TS_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_TS_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_TS_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PTS_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PTS_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PTS_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PTS_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PTS_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR7_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR7_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR7_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR7_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR7_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR8_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR8_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR8_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR8_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Bernoulli100_theta_05_to_07_PR8_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/Bernoulli100/Bernoulli100_theta_0.5_to_0.7_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Bernoulli100_theta_05_to_07_PR9_N1000_T200K_AVG = pickle.load(fd)

T = len(Bernoulli100_theta_05_to_07_TS_T200K_CUM)
label_fs = 14

#plt.figure(1)
plt.figure(1, figsize=(8, 6))
plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N100_T200K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N1000_T200K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N100_T200K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N1000_T200K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N100_T200K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N1000_T200K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_TS_T200K_CUM, color='red', linestyle='-', label = "TS")
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
plt.xlim([-5000, 100000])
plt.ylabel('cumulative regret', fontsize=label_fs)
plt.ylim([0, 4000])
plt.show() 
plt.savefig('figs_thesis/Bernoulli100_theta_0.5_to_0.7_CUM.png')


#plt.figure(2)
plt.figure(2, figsize=(8, 6))
plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N100_T200K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR7_N1000_T200K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N100_T200K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_PR8_N1000_T200K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N100_T200K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
#plt.plot(range(T), Bernoulli100_theta_05_to_07_PR9_N1000_T200K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
plt.plot(range(T), Bernoulli100_theta_05_to_07_TS_T200K_AVG, color='red', linestyle='-', label = "TS")
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
#plt.xlim([-5000, 100000])
plt.ylabel('running average regret', fontsize=label_fs)
plt.show() 
plt.savefig('figs_thesis/Bernoulli100_theta_0.5_to_0.7_AVG.png')