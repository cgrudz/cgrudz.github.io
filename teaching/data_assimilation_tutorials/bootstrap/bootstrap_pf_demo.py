import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.widgets import Slider, RadioButtons
from ipywidgets import interactive
from IPython.display import display
from matplotlib.patches import Ellipse
import copy
import ipdb

# initial paramter values
ensn_0 = 25
bstd_0 = 0.1
rstd_0 = 0.1
k_0 = 2


# color map
wmap = "plasma"

# auxiliary functions

def Ikeda(X_0, u):
    """The array X_0 will define the initial condition and the parameter u controls the chaos of the map
    
    This should return X_1 as the forward state."""
    
    t_1 = 0.4 - 6 / (1 + X_0.dot(X_0) )
    
    x_1 = 1 + u * (X_0[0] * np.cos(t_1) + X_0[1] * np.cos(t_1))
    y_1 = u * (X_0[0] * np.sin(t_1) + X_0[1] * np.cos(t_1))
                 
    X_1 = np.array([x_1, y_1])
    
    return X_1

def Ikeda_V(X_0, u):
    """The array X_0 will define the ensemble matrix of dimension 2 times N_ens
    
    This should return X_1 as the forward state."""
    
    t_1 = 0.4 - 6 / (1 + np.sum(X_0*X_0, axis=0) )
    
    x_1 = 1 + u * (X_0[0, :] * np.cos(t_1) + X_0[1, :] * np.cos(t_1))
    y_1 = u * (X_0[0, :] * np.sin(t_1) + X_0[1, :] * np.cos(t_1))
                 
    X_1 = np.array([x_1, y_1])
    
    return X_1



# run the experiment
def animate_pf(B_std, R_std, k, ens_n):

    # force to integer for indexing
    k = int(k)
    ens_n = int(ens_n)

    # define the static background and observational error covariances
    P_0 = B_std**2 * np.eye(2)
    R = R_std**2 * np.eye(2)

    # set a random seed for the reproducibility
    np.random.seed(1)
    
    # we define the mean for the background
    x_b = np.array([0,0])
    
    # and the initial condition of the real state as a random draw from the prior
    x_t = np.random.multivariate_normal(x_b, P_0)

    y_obs = np.zeros([2,k-1])
    
    # define the Ikeda map parameter
    u = 0.9
    
    for i in range(k-1):
        # we forward propagate the true state
        x_t = Ikeda(x_t, u)
    
        # and generate a noisy observation
        y_obs[:, i] = x_t + np.random.multivariate_normal([0,0], R)
    
    
    # we define the ensemble as a random draw of the prior with equal weights
    ens_a = np.random.multivariate_normal(x_b, P_0, size=ens_n).transpose()
    ens_w_f = np.ones(ens_n) / ens_n
    
    for i in range(k-1):
        
        # forward propagate the last analysis
        ens_f = Ikeda_V(ens_a, u)
        
        # store the forecast weights before update for the plotting in the final loop of the forecasts
        ens_w_f_0 = ens_w_f
        
        # compute the likelihood of the observation given the samples and update the weights
        lik = np.exp( -.5 * np.sum( (ens_f.transpose() - y_obs[:, i])**2, axis=1) / R_std**2  ) \
                / np.sqrt( (2*np.pi)**2 * np.linalg.det(R))
        ens_w_a = ens_w_f * lik

        # normalize the weights
        ens_w_a = ens_w_a / np.sum(ens_w_a)

        # compute the effective number of samples
        N_eff = 1 / np.sum(ens_w_a**2)

        # resampling
        if N_eff < (0.1 * ens_n):
            C = np.zeros(ens_n)
            
            for j in range(ens_n):
                C[j] = sum(ens_w_a[0:j+1])

            xi_1 = np.random.uniform( low=0, high=(1/ens_n) )
            m = 0

            for j in range(ens_n):
                xi = xi_1 + j * (1 / ens_n)
                
                while xi > C[m]:
                    m = m + 1
                
                ens_a[:, j] = ens_f[:,m] + np.random.multivariate_normal([0,0], np.eye(2) * 0.001)

            ens_w_a = np.ones(ens_n) / ens_n
            ens_w_f = ens_w_a

        else:
            ens_a = ens_f
            ens_w_f = ens_w_a

    return ens_f, ens_w_f_0, ens_a, ens_w_a, y_obs, x_t


# define the canvas and the window sizes
fig = plt.figure(figsize=(16,8))
axf = fig.add_axes([.07, .17, .4, .7])
axa = fig.add_axes([.53, .17, .4, .7])

ax_ens = fig.add_axes([0.2, 0.01, 0.20, 0.05])
ax_nanl = fig.add_axes([0.2, 0.07, 0.20, 0.05])
ax_bstd = fig.add_axes([0.70, 0.01, 0.20, 0.05])
ax_rstd = fig.add_axes([0.70, 0.07, 0.20, 0.05])
ax_cbar = fig.add_axes([0.5, 0.92, .4, .05])

# run the simulation with the intiial values
ens_f, ens_w_f, ens_a, ens_w_a, y_obs, x_t = animate_pf(bstd_0, rstd_0, k_0, ensn_0)

# plot the initial experiment
indx = np.argsort(ens_w_f)
ens_w_f = ens_w_f[indx]
ens_f = ens_f[:, indx]

indx = np.argsort(ens_w_a)
ens_w_a = ens_w_a[indx]
ens_a = ens_a[:, indx]

l1 = axf.scatter(ens_f[0, :], ens_f[1, :], c=ens_w_f, s=20, alpha=.5, marker=',', cmap=wmap)
l3 = axa.scatter(ens_a[0, :], ens_a[1, :], c=ens_w_a, s=20, alpha=.5, marker=',', cmap=wmap)
l2 = axa.scatter(y_obs[0, -1], y_obs[1, -1], c='r', s=46, marker='d')
l4 = axf.scatter(x_t[0], x_t[1], c='#00ffff', s=66, marker='x')

axa.add_patch(Ellipse(y_obs[:,-1], 2*rstd_0, 2*rstd_0, ec='r', fc='none'))
cmap = cm.ScalarMappable(norm=None, cmap=wmap)
plt.colorbar(cmap, cax=ax_cbar, orientation='horizontal')


# define the parameter sliders
s_ens = Slider(ax_ens, 'N_ens', 25, 200, valinit=ensn_0, valstep=25)
s_bstd = Slider(ax_bstd, 'First prior error standard deviation', .1, 1.0, valinit=bstd_0, valstep=0.1)
s_rstd = Slider(ax_rstd, 'Observation error standard deviation', .1, 1.0, valinit=rstd_0, valstep=0.1)
s_nanl = Slider(ax_nanl, 'Forecast number', 2, 100, valinit=k_0, valstep=1)


# function defines the update when parameter sliders are adjusted
def update(val):
    ensn = s_ens.val
    bstd = s_bstd.val
    rstd = s_rstd.val
    k = s_nanl.val

    ens_f, ens_w_f, ens_a, ens_w_a, y_obs, x_t = animate_pf(bstd, rstd, k, ensn)
    
    axf.cla()
    axa.cla()

    indx = np.argsort(ens_w_f)
    ens_w_f = ens_w_f[indx]
    ens_f = ens_f[:, indx]

    indx = np.argsort(ens_w_a)
    ens_w_a = ens_w_a[indx]
    ens_a = ens_a[:, indx]

    l1 = axf.scatter(ens_f[0, :], ens_f[1, :], c=ens_w_f, s=20, alpha=.5, marker=',', cmap=wmap)
    l3 = axa.scatter(ens_a[0, :], ens_a[1, :], c=ens_w_a, s=20, alpha=.5, marker=',', cmap=wmap)
    l2 = axa.scatter(y_obs[0, -1], y_obs[1, -1], c='r', s=46, marker='d')
    l4 = axf.scatter(x_t[0], x_t[1], c='#00ffff', s=66, marker='x')
    
    axa.add_patch(Ellipse(y_obs[:,-1], 2*rstd, 2*rstd, ec='r', fc='none'))

    axf.set_xlim([-2, 4])
    axa.set_xlim([-2, 4])
    axf.set_ylim([-4,2])
    axa.set_ylim([-4,2])
    fig.canvas.draw_idle()

s_ens.on_changed(update)
s_bstd.on_changed(update)
s_rstd.on_changed(update)
s_nanl.on_changed(update)


axf.set_xlim([-2, 4])
axa.set_xlim([-2, 4])
axf.set_ylim([-4,2])
axa.set_ylim([-4,2])
axa.tick_params(
        labelleft=False,
        labelright=True,
        labelsize=18)
axf.tick_params(
        labelsize=18)

ax_bstd.tick_params(
        labelsize=15)

labels = ['Observation', 'Truth']
fig.legend([l2,l4],labels, loc='upper left', ncol=2, fontsize=26)
plt.figtext(.025, .52, r'Forecast step', horizontalalignment='center', verticalalignment='center', fontsize=22, rotation='90')
plt.figtext(.975, .52, r'Analysis step', horizontalalignment='center', verticalalignment='center', fontsize=22, rotation='270')
plt.show()
    

