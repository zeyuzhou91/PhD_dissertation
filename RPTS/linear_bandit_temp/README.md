# Thompson sampling for linear bandits, a special case of Kalman filter

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
