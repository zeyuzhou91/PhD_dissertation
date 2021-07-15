import numpy as np
import matplotlib.pyplot as plt
import pickle

## D=10, theta^* = [0.2, ... , 0.2]

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

##inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N100_T200K_CUM'
##fd = open(inputFile, 'rb')
##Linear_D10_theta_02x10_PR9_N100_T200K_CUM = pickle.load(fd)

##inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N100_T200K_AVG'
##fd = open(inputFile, 'rb')
##Linear_D10_theta_02x10_PR9_N100_T200K_AVG = pickle.load(fd)

##inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N1000_T200K_CUM'
##fd = open(inputFile, 'rb')
##Linear_D10_theta_02x10_PR9_N1000_T200K_CUM = pickle.load(fd)

##inputFile = 'data/D10/Linear_D10_theta_0.2x10_PR9_N1000_T200K_AVG'
##fd = open(inputFile, 'rb')
##Linear_D10_theta_02x10_PR9_N1000_T200K_AVG = pickle.load(fd)

#T = len(Linear_D10_theta_02x10_TS_T200K_CUM)
#label_fs = 14

##plt.figure(1)
#plt.figure(1, figsize=(8, 6))
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N100_T200K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N1000_T200K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N100_T200K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N1000_T200K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Linear_D10_theta_02x10_PR9_N100_T200K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Linear_D10_theta_02x10_PR9_N1000_T200K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_TS_T200K_CUM, color='red', linestyle='-', label = r"TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('cumulative regret', fontsize=label_fs)
#plt.ylim([0, 8000])
#plt.show() 
#plt.savefig('figs_thesis/Linear10_theta_0.2x10_CUM.png')


##plt.figure(2)
#plt.figure(2, figsize=(8, 6))
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N100_T200K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR7_N1000_T200K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N100_T200K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
#plt.plot(range(T), Linear_D10_theta_02x10_PR8_N1000_T200K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
##plt.plot(range(T), Linear_D10_theta_02x10_PR9_N100_T200K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
##plt.plot(range(T), Linear_D10_theta_02x10_PR9_N1000_T200K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
#plt.plot(range(T), Linear_D10_theta_02x10_TS_T200K_AVG, color='red', linestyle='-', label = r"TS")
#plt.legend()
#plt.grid()
#plt.xlabel('t', fontsize=label_fs)
#plt.ylabel('running average regret', fontsize=label_fs)
#plt.show() 
#plt.savefig('figs_thesis/Linear10_theta_0.2x10_AVG.png')





# D=100, theta^* = [0.08, ... , 0.08]

inputFile = 'data/D100/Linear_D100_theta_0.08x100_TS_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_TS_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_TS_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_TS_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PTS_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PTS_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR7_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR7_N1000_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N100_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N100_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N100_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N100_T200K_AVG = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N1000_T200K_CUM'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N1000_T200K_CUM = pickle.load(fd)

inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR8_N1000_T200K_AVG'
fd = open(inputFile, 'rb')
Linear_D100_theta_008x100_PR8_N1000_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N100_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D100_theta_008x100_PR9_N100_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N100_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D100_theta_008x100_PR9_N100_T200K_AVG = pickle.load(fd)

#inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N1000_T200K_CUM'
#fd = open(inputFile, 'rb')
#Linear_D100_theta_008x100_PR9_N1000_T200K_CUM = pickle.load(fd)

#inputFile = 'data/D100/Linear_D100_theta_0.08x100_PR9_N1000_T200K_AVG'
#fd = open(inputFile, 'rb')
#Linear_D100_theta_008x100_PR9_N1000_T200K_AVG = pickle.load(fd)

T = len(Linear_D100_theta_008x100_TS_T200K_CUM)
label_fs = 14

#plt.figure(1)
plt.figure(1, figsize=(8, 6))
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N100_T200K_CUM, color='orange', linestyle='--', label = r"PTS, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N1000_T200K_CUM, color='orange', linestyle='-', label = r"PTS, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N100_T200K_CUM, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N1000_T200K_CUM, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N100_T200K_CUM, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N1000_T200K_CUM, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
#plt.plot(range(T), Linear_D100_theta_008x100_PR9_N100_T200K_CUM, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
#plt.plot(range(T), Linear_D100_theta_008x100_PR9_N1000_T200K_CUM, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_TS_T200K_CUM, color='red', linestyle='-', label = r"TS")
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
plt.ylabel('cumulative regret', fontsize=label_fs)
plt.ylim([0, 80000])
plt.show() 
plt.savefig('figs_thesis/Linear100_theta_0.08x100_CUM.png')


#plt.figure(2)
plt.figure(2, figsize=(8, 6))
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N100_T200K_AVG, color='orange', linestyle='--', label = r"PTS, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PTS_N1000_T200K_AVG, color='orange', linestyle='-', label = r"PTS, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N100_T200K_AVG, color='blue', linestyle='--', label = r"RPTS-1, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PR7_N1000_T200K_AVG, color='blue', linestyle='-', label = r"RPTS-1, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N100_T200K_AVG, color='green', linestyle='--', label = r"RPTS-2, $N=100$")
plt.plot(range(T), Linear_D100_theta_008x100_PR8_N1000_T200K_AVG, color='green', linestyle='-', label = r"RPTS-2, $N=1000$")
#plt.plot(range(T), Linear_D100_theta_008x100_PR9_N100_T200K_AVG, color='purple', linestyle='--', label = r"RPTS-3, $N=100$")
#plt.plot(range(T), Linear_D100_theta_008x100_PR9_N1000_T200K_AVG, color='purple', linestyle='-', label = r"RPTS-3, $N=1000$")
plt.plot(range(T), Linear_D100_theta_008x100_TS_T200K_AVG, color='red', linestyle='-', label = r"TS")
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
plt.ylabel('running average regret', fontsize=label_fs)
plt.show() 
plt.savefig('figs_thesis/Linear100_theta_0.08x100_AVG.png')