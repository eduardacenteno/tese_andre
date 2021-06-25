# -*- coding: utf-8 -*-
"""Computar e plotar as simulacoes medias de Kuramoto
   
"""

__author__ = ""
__contact__ = ""
__date__ = ""   ### Date it was created
__status__ = "Production" ### Production = still being developed. Else: Concluded/Finished.

#%%

####################
# Libraries        #
####################

# Standard imports
import time

# Third party imports
import numpy as np # 1.19.2
from matplotlib import pyplot as plt

 # Local imports
import kuramoto_module as km

#%% Define functions
def sim_mean_Kuramoto(acop_param, n_oscilators=100):
    """Essa funcao utiliza a classe de Kuramoto para retornar a media das 
    simulacoes.
    
    Parameters
    ----------
    acop_param: float
        parametro de acomplamento
        
    n_oscilators: int 
        Number of oscillators
        Default=100
    
    Returns 
    -------
    z_med: float
        Media das simulacoes
    
    """    
    # Defining time array
    t0, t1, dt = 0, 10, 0.005
    T = np.arange(t0, t1, dt)
    
    # K 
    K = [acop_param]
    
    # Main
    # Y0, W, K are initial phase, intrinsic freq and
    # coupling K matrix respectively
    Y0 = np.random.uniform(0, 2*np.pi, n_oscilators)
    W = np.random.standard_cauchy(n_oscilators)
        
    # Passing parameters as a dictionary
    init_params = {'W':W, 'K':K, 'Y0':Y0}
     
    # Running Kuramoto model
    kuramoto = km.Kuramoto(init_params)
    odePhi = kuramoto.solve(T)
     
    # Computing phase dynamics
    phaseDynamics = np.diff(odePhi)/dt
    t2 = range(0, 1999) # indices da janela
    z = np.zeros(len(t2))
    for k in range(len(t2)):
        ph = 0
        for j in range(n_oscilators):
            ph += np.exp(1j*phaseDynamics[j][t2[k]])
        z[k] = np.absolute(ph)/n_oscilators
    z_med = np.mean(z) # recebe a média temporal do parâmetro de kuramoto
   

  #  aux = np.zeros_like(phaseDynamics, dtype = complex)
   # for i, j in product(range(aux.shape[0]), range(aux.shape[1])):
    #    aux[i, j] = cmath.exp(1j*phaseDynamics[i, j])
     #   soma = np.zeros(len(aux[0]), dtype = complex)
    #for i in range(len(aux)):
     #   soma += aux[i]
    
   # r = np.zeros(len(aux[0]))
    #for i in range(len(aux)):
     #   r[i] = np.absolute(soma[i])/n_oscilators
    #s = (np.sum(r)/(t1-t0))
    return(z_med)

#sugestão: tempo de simulação, escala de acoplamento, número de osciladores. 
# Verificar na literatura.
def transition(K, n_osc):
    """
    
    Parameters
    ----------
    K: np.arange
        range de acoplamento
        
    n_osc: int
        numero de oscilacoes
        
    Returns 
    -------
    r: media do parametro
    
    """ 
    r = np.zeros(len(K))
    for i in range(len(K)):
        r[i] = sim_mean_Kuramoto(K[i], n_osc)
    return(r) #retorna o parâmetro de kuramoto para cada nível de acoplamento K

#%% Run and plot
K = np.arange(0, 1, 0.01) # range de acoplamento
r = transition(K, 10)

plt.plot(K, r, 'o')
plt.xlabel('forca de acomplamento (K)')
plt.ylabel('media do parametro de ordem (r)')
plt.show()



#### Dicas: tenta comentar/documentar o codigo o maximo para que fique cada 
#vez mais facil de lembrar como ele funciona. 

# Tenta ter variaveis com nomes que sejam meio autoexplicativos, mas que nao 
#sejam muito longos

# tenta manter cada linha no max at 72-78 caracteres.

# fica a vontade para mudar as coisas que escrevi, na documentacao, explicacoes
# nome do ylabel, xlabel etc.