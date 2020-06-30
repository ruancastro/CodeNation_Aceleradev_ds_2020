# A resposta deve conter os valores da média, mediana, moda e desvio padrão
# da pontuação de crédito para cada estado do dataset.

import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('desafio1.csv')
# conhecendo o dataset :

# print(df.head(10))
# print(df.columns)
# print(df.info())

# Análise de dados nulos : 
# print(df.isnull().sum())
# Ok nenhum dado nulo, isso é bom ! 

# Quais são os estados que estamos trabalhando ? 
# print(df['estado_residencia'].unique())
# Temos apenas três estados , SC, RS e PR.

# Observando o target (coluna 'pontuacao_credito'):

# print(df['pontuacao_credito'])
# sns.distplot(df['pontuacao_credito'])
# df['pontuacao_credito'].hist(bins=65)
# plt.xlabel("Pontuação de crédito")
# plt.ylabel("Quantidade de aparições")
# plt.show()

# sns.boxplot(x='pontuacao_credito',data=df)
# # sns.barplot
# plt.show()


# Paraná 
PR = df[df['estado_residencia'] == 'PR']

# moda , mediana , média e desvio padrão.
PR_statistcs = []

PR_statistcs.append(PR['pontuacao_credito'].mode())
PR_statistcs.append(PR['pontuacao_credito'].median())
PR_statistcs.append(PR['pontuacao_credito'].mean())
PR_statistcs.append(PR['pontuacao_credito'].std())

print('Estatísticas PR: {}\n'.format(PR_statistcs))

# Rio grande do Sul
RS = df[df['estado_residencia'] == 'RS']
# moda , mediana , média e desvio padrão.
RS_statistcs = []

RS_statistcs.append(RS['pontuacao_credito'].mode())
RS_statistcs.append(RS['pontuacao_credito'].median())
RS_statistcs.append(RS['pontuacao_credito'].mean())
RS_statistcs.append(RS['pontuacao_credito'].std())

print('Estatísticas RS: {}\n'.format(RS_statistcs))

# Santa Catarina

SC = df[df['estado_residencia'] == 'SC']
# moda , mediana , média e desvio padrão.
SC_statistcs = []

SC_statistcs.append(SC['pontuacao_credito'].mode())
SC_statistcs.append(SC['pontuacao_credito'].median())
SC_statistcs.append(SC['pontuacao_credito'].mean())
SC_statistcs.append(SC['pontuacao_credito'].std())

print('Estatísticas SC: {}\n'.format(SC_statistcs))
