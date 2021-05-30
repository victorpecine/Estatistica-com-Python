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

# montando dataframe das notas do Fulano
notas_fulano = df[['Fulano']]

nota_media_fulano = notas_fulano.mean()[0]

notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()

desvio_medio_absoluto_fulano = notas_fulano['Fulano'].mad()
# print(desvio_medio_absoluto_fulano)

notas_sicrano = df[['Sicrano']]

nota_media_sicrano = notas_sicrano.mean()[0]

notas_sicrano['Desvio'] = notas_sicrano['Sicrano'] - nota_media_sicrano
notas_sicrano['|Desvio|'] = notas_sicrano['Desvio'].abs()

desvio_medio_absoluto_sicrano = notas_sicrano['Sicrano'].mad()
# print(desvio_medio_absoluto_sicrano)

if desvio_medio_absoluto_fulano > desvio_medio_absoluto_sicrano:
    print('Fulano teve um desvio médio absoluto maior que Sicrano')
else:
    print('Sicrano teve um desvio médio absoluto maior que Fulano')