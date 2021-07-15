import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import auxiliary as aux



#colors = ['green', 'blue', 'orange', 'purple', 'gray', 'yellow']



def plot_figures(G, t):
    """
    Plot figures of the game G at time t.
    
    t:    the round index, 0 <= t <= T-1. 
    """
     
    fig1 = plt.figure(1)
    plt.clf()  # clear the current figure
    plt.ion()  # without this, plt.show() will block the code execution
    fig1.suptitle('time =' + str(t))    
    
    ax1 = plt.subplot(111)  # position graph
    plot_position_graph(G, t, ax1)
    
    #ax2 = plt.subplot(122)  # current beta distributions
    #plot_beta_distributions(G, t, ax2)
    
    #ax2 = plt.subplot(122)  # particle distribution
    #plot_particle_distributions(G, t, ax2)
    
    plt.show()
    plt.pause(0.0001)

    return None



def plot_position_graph(G, t, ax):

    # Plot the diagonal line
    arr = np.linspace(0,1,10)
    ax.plot(arr, arr, color='black', linestyle='dashed')

    # Plot the true theta
    ax.scatter([G.theta_true[0]], [G.theta_true[1]], color='red', s=50, label=r'$\theta^*$')
    
    # Plot the sampled theta
    # ax.scatter([G.theta_hat[0]], [G.theta_hat[1]], color='blue', s=20, label=r'$\hat{\theta}$')
    
    # Plot the particles
    for i in range(G.Npar):
        ax.scatter(G.Particles[i][0], G.Particles[i][1], color='black', s=h(G.w[i])*100, alpha=0.8)
    
    plt.xlim([0, 1])
    plt.ylim([0, 1])    
    plt.legend()
    ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel(r'$\theta_2$') 
    plt.grid()     
                 
    return None


   
def plot_beta_distributions(G, t, ax):

    arr = np.linspace(0,1,100)
    rv1 = st.beta(G.Alpha[0], G.Beta[0])  # the posterior distribution of theta_1
    rv2 = st.beta(G.Alpha[1], G.Beta[1])  # the posterior distribution of theta_2
    
    ax.plot(arr, rv1.pdf(arr), color='orange', label=r'post. dist. of $\theta_1$ = Beta({a},{b})'.format(a=str(int(G.Alpha[0])), b=str(int(G.Beta[0]))))
    ax.plot(arr, rv2.pdf(arr), color='green', label=r'post. dist. of $\theta_2$ = Beta({a},{b})'.format(a=str(int(G.Alpha[1])), b=str(int(G.Beta[1]))))
    
    ax.stem([G.theta_true[0]], [5], linefmt='red', markerfmt='ro', label=r'$\theta_1^*$')
    ax.stem([G.theta_true[1]], [5], linefmt='red', markerfmt='rx', label=r'$\theta_2^*$')
    
    plt.xlim([0, 1]) 
    plt.legend()
    #ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel('density') 
    plt.grid()     
                 
    return None


def plot_particle_distributions(G, t, ax):
    
    ax.scatter(G.Particles[:,0], G.w, color='orange', label=r'pmf of particles on $\theta_1$')
    ax.scatter(G.Particles[:,1], G.w, color='green', label=r'pmf of particles on $\theta_2$')
    
    ax.stem([G.theta_true[0]], [0.5], linefmt='red', markerfmt='ro', label=r'$\theta_1^*$')
    ax.stem([G.theta_true[1]], [0.5], linefmt='red', markerfmt='rx', label=r'$\theta_2^*$')    
    
    plt.xlim([0, 1])
    plt.ylim([0, 1]) 
    plt.legend()
    #ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel('probability') 
    plt.grid()     
                 
    return None



def h(x):
    if x > 0.01:
        y = x
    else:
        y = 0.01
    return y
