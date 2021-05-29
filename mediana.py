from numpy import printoptions
import pandas as pd
dados = pd.read_csv('dados.csv')

df = pd.DataFrame(data={'Fulano': [8, 10, 4, 8, 6, 10, 8],
                        'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                        'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
                  index=['Matemática',
                         'Português',
                         'Inglês',
                         'Geografia',
                         'História',
                         'Física',
                         'Química'])
df.rename_axis('Matérias', axis='columns', inplace=True)

notas_fulano = df.Fulano
# notas_fulano = notas_fulano.sort_values()

# criando um dataframe para as notas do Fulano
notas_fulano = notas_fulano.reset_index()

# n = notas_fulano.shape[0]
# elemento_mediano = (n + 1)/2
# print(f'A mediana está na posição {elemento_mediano:.0f}')

# calculando a mediana das notas do Fulano
elemento_mediano_fulano = notas_fulano.median()
print(elemento_mediano_fulano)

# calculando a mediana das notas do Beltrano
notas_beltrano = df.Beltrano.sample(6, random_state=101)
elemento_mediano_beltrano = notas_beltrano.median()
print(elemento_mediano_beltrano)

# calculando a mediana das rendas
mediana_rendas = dados.Renda.median()
print(mediana_rendas)
