import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

mediana_rendas = dados.Renda.quantile()

quartis_renda = dados.Renda.quantile([0.25, 0.5, 0.75])

decis_renda = dados.Renda.quantile([i / 10 for i in range(1, 10)])

percentis_renda = dados.Renda.quantile([i / 100 for i in range(1, 100)])

ax = sns.displot(dados.Idade,
                 hist_kws={'cumulative': True},
                 kde_kws={'cumulative': True})
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumuladas', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
plt.show()
