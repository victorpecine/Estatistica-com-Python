from scipy.special import comb
from scipy.stats import binom

# combinacoes_megasena = comb(25, 20)

# probabilidade_acerto_megasena = 1 / combinacoes_megasena

# print(combinacoes_megasena, probabilidade_acerto_megasena)

# Probabilidade de acertar 5 questões
n = 10  # numero de questões
numero_alternativas_por_questao = 3

p = 1 / numero_alternativas_por_questao  # probabilidade_acerto

q = 1 - p  # probabilidade_erro

k = 5  # total de eventos que se deseja obter sucesso


probabilidade_cinco_acertos = binom.pmf(k, n, p)
print(probabilidade_cinco_acertos)

# Probabilidade de passar no teste
probabilidade_passar_teste = binom.sf(4, n, p)
print(probabilidade_passar_teste)
