#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np
from sklearn import preprocessing
import math


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[7]:


#  Quest 1
# print(black_friday.info())
# print(black_friday.columns)
# print(len(black_friday.columns))
# print(black_friday.shape)
# print(type(black_friday.shape))


# Quest 2 

# dfq2 = black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35') ]
# x = dfq2['Gender'].value_counts().values
# x = int(x)

# Quest 3 
# black_friday['User_ID'].nunique()

# Quest 4
# print(black_friday.dtypes.nunique())

# Quest 5
# float((black_friday.isnull().sum()/len(black_friday)).max())
# print(type())
# black_friday.isnull().mean().max()

# Quest 6
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.
# black_friday.isnull().mean()
# len(black_friday[black_friday['Product_Category_3'].isnull() == True])

# Quest 7 
# Qual o valor mais frequente (sem contar nulls) em Product_Category_3? Responda como um único escalar.
# float(black_friday['Product_Category_3'].dropna().mode())

# Quest 8
# Qual a nova média da variável (coluna) Purchase após sua normalização? Responda como um único escalar.
# black_friday['Purchase']
# norm_purchase=(black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
# norm_purchase.mean()

# Quest 9
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel Purchase após sua padronização? Responda como um único escalar.
# scaler = preprocessing.StandardScaler()
# x_scaler = scaler.fit_transform(black_friday[['Purchase']])
# df_scaler = pd.DataFrame(x_scaler)
# df_scaler[(df_scaler[0] >= -1) & (df_scaler[0]<=1)].shape[0]

# Quest 10
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`)
# colunas = ['Product_Category_2','Product_Category_3']
# df_aux = black_friday[colunas]
# # print(df_aux.head(10))

# for index, row in df_aux.iterrows():
#         if (math.isnan(row['Product_Category_2']) == True) & (math.isnan(row['Product_Category_3']) == True):
#             resposta = True
#             print(resposta)
#             break


# ## Questão 1
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[108]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return (black_friday.shape)
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[56]:


def q2():
    # Retorne aqui o resultado da questão 2.
    dfq2 = black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35') ]
    x = dfq2['Gender'].value_counts().values
    return int(x[0])
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[57]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[23]:


def q4():
    # Retorne aqui o resultado da questão 4.
    x = black_friday.dtypes.nunique()
    return x
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[59]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return black_friday.isnull().mean().max()
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[60]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return len(black_friday[black_friday['Product_Category_3'].isna() == True])
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[61]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return float(black_friday['Product_Category_3'].dropna().mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[62]:


def q8():
    # Retorne aqui o resultado da questão 8.
    norm_purchase=(black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return norm_purchase.mean()
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[63]:


def q9():
    # Retorne aqui o resultado da questão 9.
    scaler = preprocessing.StandardScaler()
    x_scaler = scaler.fit_transform(black_friday[['Purchase']])
    df_scaler = pd.DataFrame(x_scaler)
    return df_scaler[(df_scaler[0] >= -1) & (df_scaler[0]<=1)].shape[0]
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[64]:


def q10():
    # Retorne aqui o resultado da questão 10.
    colunas = ['Product_Category_2','Product_Category_3']
    df_aux = black_friday[colunas]
    for index, row in df_aux.iterrows():
        if (math.isnan(row['Product_Category_2']) == True) & (math.isnan(row['Product_Category_3']) == True):
            resposta = True
            break
    return resposta
    pass

