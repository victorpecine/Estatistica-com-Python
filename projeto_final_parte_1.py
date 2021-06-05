import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('dados.csv')

conteudo_dataframe = dados.head()

renda_minima = dados.Renda.min()
renda_maxima = dados.Renda.max()
salario_minimo = 788

classes_renda = [renda_minima,
                 2 * salario_minimo,
                 5 * salario_minimo,
                 15 * salario_minimo,
                 25 * salario_minimo,
                 renda_maxima]

classes_renda_labels = ['E', 'D', 'C', 'B', 'A']

frequencia_rendas = pd.value_counts(pd.cut(x=dados.Renda,
                                           bins=classes_renda,
                                           labels=classes_renda_labels,
                                           include_lowest=True))

percentual_rendas = pd.value_counts(pd.cut(x=dados.Renda,
                                           bins=classes_renda,
                                           labels=classes_renda_labels,
                                           include_lowest=True),
                                    normalize=True) * 100

distribuicao_frequencia_rendas = pd.DataFrame({'Frequência': frequencia_rendas,
                                               'Porcentagem (%)': percentual_rendas})

# gráfico de barras
# grafico_distribuicao_frequencia_rendas = distribuicao_frequencia_rendas['Frequência'].plot.pie(width=1, color='red', alpha=0.2, figsize=(14, 6))

# gráfico pizza
# grafico_distribuicao_frequencia_rendas = plt.pie(frequencia_rendas, labels=classes_renda_labels, autopct='%1.1f%%')
# plt.show()

# histograma_rendas = sns.distplot(dados['Renda'], kde=False)
# histograma_rendas.figure.set_size_inches(12, 6)
# histograma_rendas.set_title('Distribuição de Frequências - Renda', fontsize=12)
# histograma_rendas.set_xlabel('Renda (R$)', fontsize=12)
# plt.show()

# histograma de rendas até R$ 15.000,00
# histograma_rendas = sns.distplot(dados.query('Renda < 15000')['Renda'])
# histograma_rendas.figure.set_size_inches(12, 6)
# histograma_rendas.set_title('Distribuição de Frequências - Renda', fontsize=12)
# histograma_rendas.set_xlabel('Renda (R$)', fontsize=12)
# plt.show()

sexo = {0: 'Masculino',
        1: 'Feminino'}
cor = {0: 'Indígena',
       2: 'Branca',
       4: 'Preta',
       6: 'Amarela',
       8: 'Parda',
       9: 'Sem declaração'}

frequencia_sexo_cor = pd.crosstab(dados.Sexo, dados.Cor)
frequencia_sexo_cor.rename(index=sexo, inplace=True)
frequencia_sexo_cor.rename(columns=cor, inplace=True)

percentual_sexo_cor = pd.crosstab(dados.Sexo,
                                  dados.Cor,
                                  normalize=True) * 100
percentual_sexo_cor.rename(index=sexo, inplace=True)
percentual_sexo_cor.rename(columns=cor, inplace=True)

# print(percentual_sexo_cor)

media_rendas = dados.Renda.mean()

mediana_rendas = dados.Renda.median()

moda_rendas = dados.Renda.mode()[0]

desvio_medio_abs_rendas = dados.Renda.mad()

variancia_renda = dados.Renda.var()

desvio_padrao_rendas = dados.Renda.std()

estatisticas_renda_sexo_cor = pd.crosstab(dados.Cor,
                                          dados.Sexo,
                                          values=dados.Renda,
                                          aggfunc={'mean',
                                                   'median',
                                                   'max'})
estatisticas_renda_sexo_cor.rename(index=cor, inplace=True)
estatisticas_renda_sexo_cor.rename(columns=sexo, inplace=True)
print(estatisticas_renda_sexo_cor)
