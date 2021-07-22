# Simulation for max-Bernoulli bandit

This folder contains the simulatoin code for solving the max-Bernoulli bandit problem
with the following algorithms: Thompson sampling (TS), particle Thompson sampling (PTS), 
and regenerative particle Thompson sampling (RPTS). 


## Description of files

**main.py** contains the simulation setup. Model parameters can be modified in this file.

**bandit.py** implements the main procedures in the max-Bernoulli bandit problem.

**auxuliary.py** constains some auxiliary functions. 

**model.py** constains the observation model (a distribution). 

**PTS.py** implements the particle Thompson sampling algorithm.

**RPTS.py** implements the regenerative particle Thompson sampling algorithms, including RPTS1 and RPTS2. 



## How to use

### 1. Open main.py and set the parameters. 

**N**: a positive integer, the total number of arms.

**M**: a positive integer less than N, the number of arms to be chosen at each step. 

**T**: the time horizon (number of steps in each simulation).

**N_simul**: the number of simulations to run, over which the average regret will be obtained.

**alg**: a string, the name of the algorithm. Options: 'PTS', 'RPTS1', 'RPTS2'. (TS cannot be implemented for this problem.)

**Npar**: the number of particles, only applies to PTS, RPTS1, and RPTS2. 

### 2. Open bandit.py and modify the function init_true_parameter().

theta_true is the true system paramter. You can make this parameter fixed or randomly generated. 


### 3. Open a terminal and run:

python main.py


## Simulations


The simulation results contain two graphs, one for cumulative regret and one for 
running average regret. 


## Note

For large T, or N_simul, or Npar, the simulation may take a long time. 


