import numpy as np
from scipy.special import kl_div
from scipy.stats import norm

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

def teste_kl_manual():
    ''' 
    retorna divergencia kl para dados entre distribuicoes com media 0 desvpad 2 e media 2 desvpad 2

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    '''
    x = np.arange(-10, 10, 0.001)
    p = norm.pdf(x, 0, 2)
    q = norm.pdf(x, 2, 2)
    return kl_divergence(p,q)

def teste_kl_scipy():
    ''' 
    retorna divergencia kl para dados entre distribuicoes com media 0 desvpad 2 e media 2 desvpad 2

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    '''
    x = np.arange(-10, 10, 0.001)
    p = norm.pdf(x, 0, 2)
    q = norm.pdf(x, 2, 2)
    return indice_citacao(p,q)