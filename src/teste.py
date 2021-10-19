from divergenciakl import indice_citacao
from divergenciakl import kl_divergence

x = np.arange(-10, 10, 0.001)
p = norm.pdf(x, 0, 2)
q = norm.pdf(x, 2, 2)

#resultado funcao manual
resultado1 = kl_divergence(p,q)

