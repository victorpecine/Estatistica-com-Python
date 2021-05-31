import pandas as pd

dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

variancia_altura_mulheres = dataset.groupby(['Sexo']).std().loc['M']
print(variancia_altura_mulheres)
