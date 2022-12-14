# -*- coding: utf-8 -*-
"""Projeto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H-J5A1TMu0s5Ps9Sa0Cr2uExCUOGbzLW
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
# dataframe
df = pd.read_csv('olympics_medals_country_wise.csv')
del df['ioc_code ']
df = df.rename(columns= {'countries ' : 'countries',
                        'total_total ' : 'total_total'})

df

df.info()

#Precisamos limpar os dados, ja que alguns nao sao int
clm=['summer_gold', 'summer_total', 'total_gold', 'total_total' ]
def fun(x):
    return x.replace(",", "")

for x in clm:
    df[x]=df[x].apply(fun)
df["summer_gold"]=df["summer_gold"].astype(int)
df['summer_total']=df['summer_total'].astype(int)
df['total_gold']=df['total_gold'].astype(int)
df['total_total']=df['total_total'].astype(int)

df.info()

#Países com mais medalhas de ouro
maiores_ouro = df.groupby('countries')['total_gold'].sum().nlargest(25)

plt.figure(figsize =(10, 7))
maiores_ouro.plot.bar()
plt.yticks([0,250,500,750,1000,1250],labels = ['0','250','500','750','1000', '1250'],rotation=90)
plt.xlabel("")
plt.title("Países com mais medalhas de ouro", fontsize=18)
plt.show()

#Países com menos medalhas de ouro
menores_ouro = df.groupby('countries')['total_gold'].sum().nsmallest(59)

plt.figure(figsize =(20, 6))
menores_ouro.plot.bar()
plt.yticks([0,1,2,3],labels = ['0','1','2','3'],rotation=90)
plt.xlabel("")
plt.title("Países com menos medalhas de ouro", fontsize=18)
plt.show()

#Países com mais medalhas de bronze
maiores_bronze = df.groupby('countries')['total_bronze'].sum().nlargest(20)
maiores_bronze

#Podemos afirmar que os países que o número de medalhas de bronze está correlacionado com o número de medalhas de ouro?
fig = plt.figure(figsize =(10, 7))
sns.regplot(df.total_bronze,df.total_gold, ci=None)
correlation = df.total_bronze.corr(df.total_gold)

plt.yticks([0,500,1000,1500], labels = ['0','500','1000','1500'],rotation=90)
plt.xticks([0,500,1000], labels = ['0','500','1000'])

plt.xlabel("Bronze")
plt.ylabel("Ouro")
plt.text(1.00e+3,1.5e+3,'Correlation = {:.2f}'.format(correlation))
plt.show()