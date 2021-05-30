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

notas_fulano = df[['Fulano']]
nota_media_fulano = notas_fulano.mean()[0]
notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)

variancia_notas_fulano = notas_fulano['Fulano'].var()
print(variancia_notas_fulano)
