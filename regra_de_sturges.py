import pandas as pd
import numpy as np
dados = pd.read_csv('dados.csv')

quantidade_de_registros = dados.shape[0]
quantidade_de_variaveis = dados.shape[1]
k = 1 + (10/3) * np.log10(quantidade_de_registros)
# print(f'Quantidade de registro: {quantidade_de_registros}\n'
#       f'Quantidade de variáveis: {quantidade_de_variaveis}\n'
#       f'Quantidade de classes: {int(k.round(0))}\n')

frequencia = pd.value_counts(
                pd.cut(
                       x=dados.Renda,
                       bins=int(k.round(0)),
                       include_lowest=True
                       ),
                sort=False
                )
# print(frequencia)

percentual = pd.value_counts(
                pd.cut(
                       x=dados.Renda,
                       bins=int(k.round(0)),
                       include_lowest=True
                       ),
                sort=False,
                normalize=True
                )*100
# print(percentual)

distribuicao_frequencias_amplitude_fixa = pd.DataFrame(
                                                       {'Frequência': frequencia,
                                                        'Porcentagem (%)': percentual}
                                                       )
print(distribuicao_frequencias_amplitude_fixa)
