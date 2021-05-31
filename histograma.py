import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

# histograma com seaborn
ax = sns.histplot(dados.Altura, kde=False)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros (m)', fontsize=14)
plt.show()

# histograma com pandas
# dados.Altura.hist(bins=50, figsize=(12, 6))
# plt.show()
