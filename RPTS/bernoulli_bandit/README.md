# Thompson sampling for linear bandits, a special case of Kalman filter (TO BE UPDATED)

This folder contains the simulation program of a linear bandit problem solved 
by Thompson sampling, implemented as a special case of Kalman filter. 

## Description of files

main.py contains the simulation setup. Model parameters can be modified in this file.

Game.py implements the main body of the linear bandit model, with the main class System. 

Thompson_Sampling.py implements the Thompson sampling algorithm, with a sub-class System_TS.

myplot.py implements functions for plotting figures, useful for showing animated dynamics of results. 

Particle_Thompson_Sampling.py implements the Particle Thompson sampling algorithm, currently not used (to be modifed later). 

auxuliary.py contains some auxiliary functions, currently empty. 

test.py is a test program for plotting the contours of a Gaussian distribution. 

## How to use

### Open main.py and set the parameters: 

N: a positive integer, the number of dimensions of parameters and actions. 

T: the time horizon (number of steps in each simulation)

N_simul: the number of simulations to run, over which the average regret will be obtained

### Open a terminal and run:

python main.py

## Simulations


