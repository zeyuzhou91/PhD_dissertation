# A contextual bandit model for network slicing - Model 2

This folder contains the simulation program of a contextual bandit model for 
network slicing. 

## Description of files

main.py contains the simulation setup. Model parameters can be modified in this file.

Game.py implements the main body of a contextual bandit model for network slicing, with the main class System. 

Particle_Thompson_Sampling.py implements the particle Thompson sampling algorithm, with two sub-classes System_PTS1 and System_PTS2. System_PTS1 generates per-system particles. System_PTS2 generates per-block particles. 

auxuliary.py contains some auxiliary functions. 

## How to use

### Open main.py and set the parameters: 

D: a positive integer, number of domains

B: a positive integer list, the number of resource blocks in each domain

t: the time horizon (number of steps in each simulation)

N_simul: the number of simulations to run, over which the average regret will be obtained

### Open a terminal and run:

python main.py
