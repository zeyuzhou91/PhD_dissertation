# Simulation for Bernoulli bandit

This folder contains the simulatoin code for solving the linear bandit problem
with the following algorithms: Thompson sampling (TS), particle Thompson sampling (PTS), 
and regenerative particle Thompson sampling (RPTS). 

## Description of files

**main.py** contains the simulation setup. Model parameters can be modified in this file.

**bandit.py** implements the main procedures in the linear bandit problem.

**auxuliary.py** constains some auxiliary functions. 

**model.py** constains the observation model (a distribution). 

**Thompson_Sampling.py** implements the Thompson sampling algorithm as a special case of Kalman filter. 

**PTS.py** implements the particle Thompson sampling algorithm.

**RPTS.py** implements the regenerative particle Thompson sampling algorithms, including RPTS1 and RPTS2. 



## How to use

### 1. Open main.py and set the parameters. 

**K**: a positive integer, the dimension of the parameter space. 

**var_W**: a positive real values, the variance of the noise W. 

**T**: the time horizon (number of steps in each simulation).

**N_simul**: the number of simulations to run, over which the average regret will be obtained.

**alg**: a string, the name of the algorithm. Options: 'TS', 'PTS', 'RPTS1', 'RPTS2'.

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















# Thompson sampling for linear bandits, a special case of Kalman filter

This folder contains the simulation program of a linear bandit problem solved 
by Thompson sampling, implemented as a special case of Kalman filter. 

## Description of files

main.py contains the simulation setup. Model parameters can be modified in this file.

.py implements the main body of the linear bandit model, with the main class System. 

Thompson_Sampling.py implements the Thompson sampling algorithm, with a sub-class System_TS.

myplot.py implements functions for plotting figures, useful for showing animated dynamics of results. 

Particle_Thompson_Sampling.py implements the Particle Thompson sampling algorithm, currently not used (to be modifed later). 

auxuliary.py contains some auxiliary functions, currently empty. 

test.py is a test program for plotting the contours of a Gaussian distribution. 

## How to use

### Open main.py and set the parameters: 

N: a positive integer, the number of dimensions of parameters and actions. 

var_W: a positive value, the variance of the observation noise. 

T: the time horizon (number of steps in each simulation)

N_simul: the number of simulations to run, over which the average regret will be obtained

### Open a terminal and run:

python main.py

## Simulations

### One particular simulation with animated dynamics

N = 2, var_W = 0.1

Available on Youtube: https://youtu.be/z_GaRqiRd4k

### The running average regret averaged over 100 simulations

N = 10, var_W = 0.5

![N=10](https://user-images.githubusercontent.com/4511007/104259449-0f3d0300-5447-11eb-9646-287f5b25023d.png)
