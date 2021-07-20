import numpy as np
import matplotlib.pyplot as plt
import pickle


inputFile = 'data/network_slicing_model1_3_3_3_PTS_a_N100_CUM'
fd = open(inputFile, 'rb')
PTS_a_N100_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_a_N100_AVG'
fd = open(inputFile, 'rb')
PTS_a_N100_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_a_N500_CUM'
fd = open(inputFile, 'rb')
PTS_a_N500_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_a_N500_AVG'
fd = open(inputFile, 'rb')
PTS_a_N500_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_b_N100_CUM'
fd = open(inputFile, 'rb')
PTS_b_N100_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_b_N100_AVG'
fd = open(inputFile, 'rb')
PTS_b_N100_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_b_N500_CUM'
fd = open(inputFile, 'rb')
PTS_b_N500_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_PTS_b_N500_AVG'
fd = open(inputFile, 'rb')
PTS_b_N500_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_a_N100_CUM'
fd = open(inputFile, 'rb')
RPTS2_a_N100_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_a_N100_AVG'
fd = open(inputFile, 'rb')
RPTS2_a_N100_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_a_N500_CUM'
fd = open(inputFile, 'rb')
RPTS2_a_N500_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_a_N500_AVG'
fd = open(inputFile, 'rb')
RPTS2_a_N500_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_b_N100_CUM'
fd = open(inputFile, 'rb')
RPTS2_b_N100_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_b_N100_AVG'
fd = open(inputFile, 'rb')
RPTS2_b_N100_AVG = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_b_N500_CUM'
fd = open(inputFile, 'rb')
RPTS2_b_N500_CUM = pickle.load(fd)

inputFile = 'data/network_slicing_model1_3_3_3_RPTS2_b_N500_AVG'
fd = open(inputFile, 'rb')
RPTS2_b_N500_AVG = pickle.load(fd)


T = len(PTS_a_N100_CUM)
label_fs = 14


plt.figure(1, figsize=(8, 6))
plt.plot(range(T), PTS_a_N100_CUM, color='orange', linestyle='--', label = "PTS, 100 per-system particles") 
plt.plot(range(T), PTS_a_N500_CUM, color='orange', linestyle='-', label = "PTS, 500 per-system particles") 
plt.plot(range(T), PTS_b_N100_CUM, color='purple', linestyle='--', label = "PTS, 100 per-block particles")
plt.plot(range(T), PTS_b_N500_CUM, color='purple', linestyle='-', label = "PTS, 500 per-block particles")
plt.plot(range(T), RPTS2_a_N100_CUM, color='green', linestyle='--', label = "RPTS-2, 100 per-system particles")
plt.plot(range(T), RPTS2_a_N500_CUM, color='green', linestyle='-', label = "RPTS-2, 500 per-system particles") 
plt.plot(range(T), RPTS2_b_N100_CUM, color='blue', linestyle='--', label = "RPTS-2, 100 per-block particles") 
plt.plot(range(T), RPTS2_b_N500_CUM, color='blue', linestyle='-', label = "RPTS-2, 500 per-block particles") 
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
plt.xlim([-100, 4000])
plt.ylabel('cumulative regret', fontsize=label_fs)
plt.ylim([0, 400])
plt.show() 
plt.savefig('figs/model1_CUM.png')


plt.figure(2, figsize=(8, 6))
plt.plot(range(T), PTS_a_N100_AVG, color='orange', linestyle='--', label = "PTS, 100 per-system particles") 
plt.plot(range(T), PTS_a_N500_AVG, color='orange', linestyle='-', label = "PTS, 500 per-system particles") 
plt.plot(range(T), PTS_b_N100_AVG, color='purple', linestyle='--', label = "PTS, 100 per-block particles")
plt.plot(range(T), PTS_b_N500_AVG, color='purple', linestyle='-', label = "PTS, 500 per-block particles")
plt.plot(range(T), RPTS2_a_N100_AVG, color='green', linestyle='--', label = "RPTS-2, 100 per-system particles")
plt.plot(range(T), RPTS2_a_N500_AVG, color='green', linestyle='-', label = "RPTS-2, 500 per-system particles") 
plt.plot(range(T), RPTS2_b_N100_AVG, color='blue', linestyle='--', label = "RPTS-2, 100 per-block particles") 
plt.plot(range(T), RPTS2_b_N500_AVG, color='blue', linestyle='-', label = "RPTS-2, 500 per-block particles") 
plt.legend()
plt.grid()
plt.xlabel('t', fontsize=label_fs)
plt.xlim([-100, 4000])
plt.ylabel('running average regret', fontsize=label_fs)
plt.show() 
plt.savefig('figs/model1_AVG.png')


