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
    
    ax1 = plt.subplot(111)  
    plot_position_graph(G, t, ax1)
    #plot_Gaussian_contour_graph(G, t, ax1)
    #plot_particle_histogram(G, t, ax1)
    

    
    plt.show()
    plt.pause(0.001)

    return None




def plot_position_graph(G, t, ax):

    # Plot the diagonal line
    arr = np.linspace(0,2*np.pi,100)
    ax.plot(np.cos(arr), np.sin(arr), color='black', linestyle='dashed')

    # Plot the true theta
    ax.scatter([G.theta_true[0]], [G.theta_true[1]], color='red', s=50, label=r'$\theta^*$')
    
    # Plot the sampled theta
    # ax.scatter([G.theta_hat[0]], [G.theta_hat[1]], color='blue', s=20, label=r'$\hat{\theta}$')
    
    # Plot the particles
    for i in range(G.Npar):
        ax.scatter(G.Particles[i][0], G.Particles[i][1], color='black', s=h(G.w[i])*100, alpha=0.8)
    
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])    
    plt.legend()
    ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel(r'$\theta_2$') 
    plt.grid()     
                 
    return None



def plot_Gaussian_contour_graph(G, t, ax):
    """
    Plot the contours of the posterior Gaussian distribution at time t. 
    
    t:    the round index, 0 <= t <= T-1. 
    """
    
    xl = -1.0
    xr = 1.0
    yl = -1.0
    yr = 1.0

    # Plot the true theta
    ax.scatter(G.theta_true[0], G.theta_true[1], c='red', s=100, alpha=1.0, label=r'$\theta^*$')
    
    # Plot the contour of the current posterior distribution
    x, y = np.mgrid[xl:xr:.01, yl:yr:.01]
    pos = np.dstack((x, y))
    rv = st.multivariate_normal(G.theta_bar, G.Sigma)
    ax.contourf(x, y, rv.pdf(pos), cmap='gray', alpha=0.6)
    ax.scatter(G.theta_bar[0], G.theta_bar[1], c = 'green', label= r'$\bar{\theta}$')

    # Plot the sampled theta
    ax.scatter(G.theta_hat[0], G.theta_hat[1], c = 'blue', label= r'$\widehat{\theta}$')
    
    plt.xlim([xl, xr])
    plt.ylim([yl, yr])    
    plt.legend()
    ax.set_xlabel(r'$\theta_1$')
    ax.set_ylabel(r'$\theta_2$') 
    plt.grid()     
    
    return None


def plot_num_of_dying_particles(G, t, ax):
    """
    DESCRIPTION HERE. 
    
    t:    the round index, 0 <= t <= T-1. 
    """
    
    num_dying = sum(G.w < (0.01/G.Npar))

    # Plot the true theta
    ax.hist(G.w, bins)
    
    #plt.xlim([xl, xr])
    plt.ylim([0, G.Npar])    
    #plt.legend()
    ax.set_xlabel('weight')
    ax.set_ylabel('# of particles') 
    plt.grid()     
    
    return None



def plot_particle_histogram(G, t, ax):
    """
    DESCRIPTION HERE. 
    
    t:    the round index, 0 <= t <= T-1. 
    """
    
    num_dying = sum(G.w < (0.01/G.Npar))
    bins = [0, 0.00001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    # Plot the true theta
    ax.hist(G.w, bins)
    
    #plt.xlim([xl, xr])
    plt.ylim([0, 20])    
    #plt.legend()
    ax.set_xlabel('weight')
    ax.set_ylabel('# of particles') 
    ax.set_title('# of particles with weight less than 0.01/1000 =' + str(num_dying))
    plt.grid()     
    
    return None




def h(x):
    if x > 0.01:
        y = x
    else:
        y = 0.01
    return y