# Simulation for network slicing model 2

This folder contains the simulatoin code for network slicing model 2, a contextual 
stochastic bandit model. 

## Description of files

**main.py** contains the simulation setup. Model parameters can be modified in this file.

**bandit.py** implements the main procedures in the stochasic bandit model. 

**auxiliary.py** constains some auxiliary functions. 

**PTS.py** implements the particle Thompson sampling algorithm, including PTS_a and PTS_b, PTS with per-system and per-block particles repectively. 

**RPTS.py** implements the regenerative particle Thompson sampling algorithms, including RPTS2_a and RPTS2_b, RPTS with per-system and per-block particles respectively.  



## How to use

### 1. Open main.py and set the parameters. 

**D**: a positive integer, the number of domains. 

**B**: a length-D list of positive integers, containing the number of resource blocks in each domain.

**T**: the time horizon (number of steps in each simulation).

**N_simul**: the number of simulations to run, over which the average regret will be obtained.

**alg**: a string, the name of the algorithm. Options: 'PTS_a', 'PTS_b', 'RPTS2_a', 'RPTS2_b'.

**Npar**: the number of (per-system or per-block) particles.


### 2. Open bandit.py and modify the function init_true_parameter().

theta_true is the true system paramter. You can make this parameter fixed or randomly generated. The default is random generation. 


### 3. Open a terminal and run:

python main.py


## Simulations


The simulation results contain two graphs, one for cumulative regret and one for 
running average regret. 


## Note

For large T, or N_simul, or Npar, the simulation may take a long time. 
