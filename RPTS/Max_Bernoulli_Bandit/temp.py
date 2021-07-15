import pickle

K = 10
M = 3
alg = 'PTS'
Npar=1000

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_1'
fd = open(inputFile, 'rb')
x1 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_2'
fd = open(inputFile, 'rb')
x2 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_3'
fd = open(inputFile, 'rb')
x3 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_4'
fd = open(inputFile, 'rb')
x4 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_5'
fd = open(inputFile, 'rb')
x5 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_6'
fd = open(inputFile, 'rb')
x6 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_7'
fd = open(inputFile, 'rb')
x7 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_8'
fd = open(inputFile, 'rb')
x8 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_9'
fd = open(inputFile, 'rb')
x9 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_CUM_10'
fd = open(inputFile, 'rb')
x10 = pickle.load(fd)

x = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10

fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + 'theta_0.51_to_0.60_' + alg + '_N' + str(Npar) + '_T200K_CUM', 'wb')
pickle.dump(x, fw)
fw.close()

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_1'
fd = open(inputFile, 'rb')
y1 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_2'
fd = open(inputFile, 'rb')
y2 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_3'
fd = open(inputFile, 'rb')
y3 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_4'
fd = open(inputFile, 'rb')
y4 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_5'
fd = open(inputFile, 'rb')
y5 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_6'
fd = open(inputFile, 'rb')
y6 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_7'
fd = open(inputFile, 'rb')
y7 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_8'
fd = open(inputFile, 'rb')
y8 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_9'
fd = open(inputFile, 'rb')
y9 = pickle.load(fd)

inputFile = 'Bernoulli10_Max3_theta_0.51_to_0.60_PTS_N1000_T200K_AVG_10'
fd = open(inputFile, 'rb')
y10 = pickle.load(fd)

y = (y1+y2+y3+y4+y5+y6+y7+y8+y9+y10)/10

fw = open('data/Bernoulli' + str(K) + '_Max' + str(M) + '/Bernoulli' + str(K) + '_Max' + str(M) + '_' + 'theta_0.51_to_0.60_' + alg + '_N' + str(Npar) + '_T200K_AVG', 'wb')
pickle.dump(y, fw)
fw.close()