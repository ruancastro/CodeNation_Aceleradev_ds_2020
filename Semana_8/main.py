#importando as bibliotecas
import pandas as pd
import numpy as np
import sklearn as sk

df_train = pd.read_csv('/home/ruan/codenation/enem-2/train.csv')
df_test = pd.read_csv('/home/ruan/codenation/enem-2/test.csv')

#  Explorando os datasets 

# print(df_train.describe())
# print(len(df_train.columns)) # 167
# print(len(df_test.columns))  # 47 
x=0
columns_test = list(df_test.columns)
for col in columns_test:
    if col in df_train:
        x=x+1

# if x==47:
#     print("df_train e df_test têm as mesmas colunas\n")
# else:
#     print("Existem {} colunas diferentes\n",47-x)

# Já que as colunas presentes no df_test estão presentes no df_train, irei simplesmente dropar as colunas excedentes.

for col in df_train.columns:
    if not(col in df_test):
        df_train.drop(col,axis=1,inplace=True)

# Checando o número de colunas, se tudo ok len(df_train.columns) == 47
# print(len(df_train.columns) == 47) #True

# Analisando os dados nulos presentes em ambos os datasets

df_nan = pd.DataFrame(columns=['train_nan','train_nan(%)','test_nan','test_nan(%)','dtypes'])
df_nan['train_nan'] = df_train.isna().sum()
df_nan['train_nan(%)'] = df_train.isna().mean()
df_nan['test_nan'] = df_test.isna().sum()
df_nan['test_nan(%)'] = df_test.isna().mean()
df_nan['dtypes'] = df_train.dtypes

# print(df_nan.head(20))

exists_nan = []
for ind in df_nan.index:
    try:
        if df_nan.loc[ind,'train_nan'] != 0:
            exists_nan.append(ind)
    except:
        pass

print(df_nan.loc[exists_nan,:])
# Algumas colunas coo 