from divergenciakl import indice_citacao
from divergenciakl import kl_divergence
from scipy.stats import norm
import numpy as np
import timeit

x = np.arange(-10, 10, 0.001)
p = norm.pdf(x, 0, 2)
q = norm.pdf(x, 2, 2)

#resultado funcao manual
resultado1 = kl_divergence(p,q)

#resultado com funcao do scipy
resultado2 = indice_citacao(p,q)

#testes
tempo_scipy = timeit.timeit('teste_kl_scipy()',setup='from divergenciakl import teste_kl_scipy',number=100)
tempo_manual = timeit.timeit('teste_kl_manual()',setup='from divergenciakl import teste_kl_manual',number=100)
print("tempo scipy:",tempo_scipy)
print("tempo manual:",tempo_manual)
print("a funcao do scipy e mais eficiente em %:",(tempo_manual-tempo_scipy)/tempo_manual)