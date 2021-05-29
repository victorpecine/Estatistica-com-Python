import pandas as pd
dados = pd.read_csv('dados.csv')

# calculando a média do Fulano
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

media_fulano = df['Fulano'].mean()
print(media_fulano)

# calculando a medía das rendas
media_renda = dados.Renda.mean()
print(media_renda)

# calculando a média das rendas por sexo
media_renda_por_sexo = dados.groupby(['Sexo'])['Renda'].mean()
media_renda_por_sexo.rename(
                            index={0: 'Masculino',
                                   1: 'Feminino'},
                            inplace=True)

print(media_renda_por_sexo)

# calculando a média das idades por sexo
dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

media_idades = dataset.groupby(['Sexo'])['Idade'].mean()
print(media_idades)
