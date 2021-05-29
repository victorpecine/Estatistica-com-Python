import pandas as pd
dados = pd.read_csv('dados.csv')
# print(dados)

anos_de_estudo = dados['Anos de Estudo'].unique()
# print(sorted(anos_de_estudo))

idade_minima = dados.Idade.min()
idade_maxima = dados.Idade.max()
# print(f'As idades variam de {idade_minima} até {idade_maxima} anos')

contagem_sexo = dados['Sexo'].value_counts()
# print(contagem_sexo)

percentual_sexo = dados['Sexo'].value_counts(normalize=True)*100
# print(contagem_sexo)

# criando um dataframe dos sexos
distribuicao_de_frequencias_qualitativas = pd.DataFrame({'Frequência':
                                                         contagem_sexo,
                                                         'Porcentagem (%)':
                                                         percentual_sexo})
# print(distribuicao_de_frequencias_qualitativas)

distribuicao_de_frequencias_qualitativas.rename(
                                                index={0: 'Masculino',
                                                       1: 'Feminino'},
                                                inplace=True)
distribuicao_de_frequencias_qualitativas.rename_axis(
                                                     'Sexo', axis='columns',
                                                     inplace=True)
# print(distribuicao_de_frequencias_qualitativas)

sexo = {0: 'Masculino',
        1: 'Feminino'}
cor = {0: 'Indígena',
       2: 'Branca',
       4: 'Preta',
       6: 'Amarela',
       8: 'Parda',
       9: 'Sem declaração'}
frequencia = pd.crosstab(dados.Sexo,
                         dados.Cor)
frequencia.rename(index=sexo, inplace=True)
frequencia.rename(columns=cor, inplace=True)
# print(frequencia)

percentual_cor = pd.crosstab(dados.Sexo,
                             dados.Cor,
                             normalize=True)*100
percentual_cor.rename(index=sexo, inplace=True)
percentual_cor.rename(columns=cor, inplace=True)
# print(percentual_cor)

percentual_renda = pd.crosstab(dados.Sexo,
                               dados.Cor,
                               aggfunc='mean',
                               values=dados.Renda)
percentual_renda.rename(index=sexo, inplace=True)
percentual_renda.rename(columns=cor, inplace=True)
# print(percentual_renda)

menor_renda = dados.Renda.min()
maior_renda = dados.Renda.max()

# print(menor_renda, maior_renda)

# os valores enter 0 e 200000 foram passados durante o curso
classes_de_renda = [0, 1576, 3152, 7880, 15760, 200000]
labels_das_classes = ['E', 'D', 'C', 'B', 'A']

frequencia_por_renda = pd.value_counts(
                                     pd.cut(x=dados.Renda,
                                            bins=classes_de_renda,
                                            labels=labels_das_classes,
                                            include_lowest=True))
# print(frequencia_por_renda)

percentual_por_renda = pd.value_counts(
                                     pd.cut(x=dados.Renda,
                                            bins=classes_de_renda,
                                            labels=labels_das_classes,
                                            include_lowest=True),
                                     normalize=True)*100
# print(percentual_por_renda)

distribuicao_de_frequencias_quantitativas = pd.DataFrame(
                                                         {'Frequência':
                                                          frequencia_por_renda,
                                                          'Porcentagem (%)':
                                                          percentual_por_renda}
                                                          ).sort_index(ascending=False)
print(distribuicao_de_frequencias_quantitativas)
