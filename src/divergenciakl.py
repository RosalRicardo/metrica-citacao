import numpy as np
from scipy.stats import norm
from scipy.special import kl_div
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

#função manual da divergência KL
def kl_divergence(p, q):
    '''
    Retorna a divergencia KL entre duas distribuições (calculado com numpy).

            Parameters:
                    p (array): distribuição de probabilidade
                    q (array): distribuição de probabilidade

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    '''
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

#função da livraria KL
def indice_citacao(p,q):
    '''
    Retorna a divergencia KL entre duas distribuições (tem o scipy.special.kl_div como dependencia).

            Parameters:
                    p (array): distribuição de probabilidade
                    q (array): distribuição de probabilidade

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    '''
    
    return kl_div(p,q)