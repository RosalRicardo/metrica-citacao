using StatsBase, Distributions, Random, BenchmarkTools

function indice_metrica(p,q)
    """
    Retorna a divergencia KL entre duas distribuições.

            Parameters:
                    p (array): distribuição de probabilidade
                    q (array): distribuição de probabilidade

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    """
    return StatsBase.kldivergence(p,q) 
end

function teste_kl()
    """
    retorna divergencia kl para dados entre distribuicoes com media 0 desvpad 2 e media 2 desvpad 2

            Returns:
                    divergencia kl (scalar): retorna valor que escalar que pode ser interpretado como a divergencia entre as distribuições
    """
    x = -10:0.001:10
    p = pdf(Normal(0,2),x)
    q = pdf(Normal(2,2),x)
    return StatsBase.kldivergence(p,q) 
end

println(teste_kl())

@btime teste_kl()
