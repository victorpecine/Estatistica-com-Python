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
                             normalize=True
                             )*100
percentual_cor.rename(index=sexo, inplace=True)
percentual_cor.rename(columns=cor, inplace=True)
# print(percentual_cor)

percentual_renda = pd.crosstab(dados.Sexo,
                               dados.Cor,
                               aggfunc='mean',
                               values=dados.Renda
                               )
percentual_renda.rename(index=sexo, inplace=True)
percentual_renda.rename(columns=cor, inplace=True)
print(percentual_renda)
