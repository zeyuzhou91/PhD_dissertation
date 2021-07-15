import pickle


inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_1'
fd = open(inputFile, 'rb')
x1 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_2'
fd = open(inputFile, 'rb')
x2 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_3'
fd = open(inputFile, 'rb')
x3 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_4'
fd = open(inputFile, 'rb')
x4 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_5'
fd = open(inputFile, 'rb')
x5 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_6'
fd = open(inputFile, 'rb')
x6 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_7'
fd = open(inputFile, 'rb')
x7 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_8'
fd = open(inputFile, 'rb')
x8 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_9'
fd = open(inputFile, 'rb')
x9 = pickle.load(fd)

inputFile = 'Bernoulli10_theta_0.51_to_0.60_PR4_N1000_T100K_AVG_10'
fd = open(inputFile, 'rb')
x10 = pickle.load(fd)


x = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/2

K=10
alg='PR4'
Npar=1000
fw = open('data/Bernoulli' + str(K) + '_T100K' + '/Bernoulli' + str(K) + '_' + 'theta_0.51_to_0.60_' + alg + '_N' + str(Npar) + '_T100K' + '_AVG', 'wb')
pickle.dump(x, fw)
fw.close()