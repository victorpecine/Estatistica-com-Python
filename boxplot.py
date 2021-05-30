import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

# ax = sns.boxplot(x='Altura', data=dados, orient='h')
# ax.figure.set_size_inches(12, 4)
# ax.set_title('Altura', fontsize=18)
# ax.set_xlabel('Metros (m)', fontsize=14)
# plt.show()

# ax = sns.boxplot(x='Altura', y='Sexo', data=dados, orient='h')
# ax.figure.set_size_inches(12, 4)
# ax.set_title('Altura', fontsize=18)
# ax.set_xlabel('Metros (m)', fontsize=14)
# plt.show()

# ax = sns.boxplot(x='Renda', data=dados, orient='h')
# ax.figure.set_size_inches(12, 4)
# ax.set_title('Renda', fontsize=18)
# ax.set_xlabel('R$', fontsize=14)
# plt.show()

# ax = sns.boxplot(x='Renda', data=dados.query('Renda < 10000'), orient='h')
# ax.figure.set_size_inches(12, 4)
# ax.set_title('Renda', fontsize=18)
# ax.set_xlabel('R$', fontsize=14)
# plt.show()

ax = sns.boxplot(x='Renda', y='Sexo', data=dados.query('Renda < 10000'),
                 orient='h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
plt.show()
