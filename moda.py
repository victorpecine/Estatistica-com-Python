from numpy import printoptions
import pandas as pd
dados = pd.read_csv('dados.csv')

# df = pd.DataFrame(data={'Fulano': [8, 10, 4, 8, 6, 10, 8],
#                         'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
#                         'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
#                   index=['Matemática',
#                          'Português',
#                          'Inglês',
#                          'Geografia',
#                          'História',
#                          'Física',
#                          'Química'])
# df.rename_axis('Matérias', axis='columns', inplace=True)

# notas_fulano = df.Fulano
# moda_notas_fulano = notas_fulano.mode()
# print(moda_notas_fulano)


# moda_rendas = dados.Renda.mode()
# print(moda_rendas)

# moda_altura = dados.Altura.mode()
# print(moda_altura)

df_lanches = pd.DataFrame(data={'Pedidos': ['Big Mac',
                                            'Quarteirão',
                                            'Big Mac',
                                            'Big Mac',
                                            'Cheeseburguer',
                                            'Big Mac',
                                            'Quarteirão',
                                            'Quarteirão',
                                            'Mc Fish',
                                            'Quarteirão',
                                            'Cheeseburguer']})

moda_pedidos = df_lanches.Pedidos.mode()
print(moda_pedidos)
