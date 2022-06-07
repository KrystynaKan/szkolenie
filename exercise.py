import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

data_adult = pd.read_csv('adult-all.csv',header=None)
data_adult.columns = [
    'age',                          #checked
    'employment',
    'some id',
    'education',
    4,                              #deleted
    'civil status history',
    'profession',
    'relationship',
    'skin colour',
    'sex',
    10,                              #deleted
    11,                              #deleted
    'working time hours/week',
    'country',
    'annual income'
]
# print(data_adult)
# print(data_adult.sample(15))

data_adult = data_adult.drop(columns=[4,10,11])

# print(data_adult.iloc[:15, :6])
# print(data_adult.iloc[:15, 6:12])

# print(data_adult['age'][data_adult['age']<18])

data_adult = data_adult[data_adult['age']>=18]
# print(data_adult['age'].unique())
# print(data_adult.info())
data_adult = data_adult.drop_duplicates()

# print(data_adult.groupby('age').agg({'age':'count'}))
data_adult = data_adult[data_adult['country'] != '?']
# print(len(data_adult[data_adult['country']=='?']))

#age checked
plt.plot(data_adult.groupby('age').agg({'age':'count'}))
# plt.show()


# print(len(data_adult[data_adult['employment']=='?']))
# print(data_adult['education'].unique())
# print(data_adult['civil status history'].unique())
# print(data_adult['profession'].unique())
# print(data_adult['relationship'].unique())
# print(data_adult['skin colour'].unique())
# print(data_adult['sex'].unique())
# print(data_adult['working time hours/week'].max())
# print(data_adult['country'].unique())
# print(data_adult['annual income'].unique())

bins = [0, 10, 30, 50, 99]
labels = ['odd job','part-time job','full-time job', 'workaholism']
data_adult['Work time categories'] = pd.cut(data_adult['working time hours/week'], bins, labels =labels)
# print(data_adult)
# print(len(data_adult[data_adult['Work time categories'] == 'workaholism']))
# print(data_adult.groupby('Work time categories').agg({'Work time categories': 'count', 'age':'mean'}))

# print(data_adult.info())

data_adult['employment'] = data_adult['employment'].replace('?','Not defined')


#COUNTRY
data_adult['country'] = data_adult['country'].replace('Hong','Hongkong')
data_adult['country'] = data_adult['country'].replace('South','South Korea')
# print(data_adult[data_adult['country'] == 'South'].groupby('skin colour').agg({'skin colour':'count'}))
# print(data_adult['country'].unique())

Europe =             ['England', 'Germany', 'Italy', 'Poland', 'Portugal', 'France', 'Scotland',
                     'Greece', 'Ireland', 'Hungary', 'Holand-Netherlands', 'Yugoslavia']
Asia =               ['China', 'Japan', 'India', 'South Korea', 'Iran', 'Philippines', 'Cambodia',
                     'Thailand', 'Laos', 'Taiwan', 'Vietnam', 'Hongkong']
North_America =      ['United-States', 'Outlying-US(Guam-USVI-etc)', 'Canada', 'Mexico', 'Puerto-Rico']
Central_America =    ['Cuba', 'Jamaica', 'Haiti', 'Dominican-Republic', 'Nicaragua', 'Honduras',
                     'El-Salvador', 'Guatemala']
South_America =      ['Trinadad&Tobago', 'Columbia', 'Ecuador', 'Peru']
continents = [Europe, Asia, North_America,Central_America,South_America]
continents_labels = ['Europe', 'Asia', 'North_America','Central_America','South_America']
data_adult['continent'] = 'NaN'
# print(continents_labels[1])
# print(data_adult['country'].iloc[1])

for i in range(len(data_adult)):
    for j in continents:
        if data_adult['country'].iloc[i] in j:
            data_adult['continent'].iloc[i] = continents_labels[(continents.index(j))]

# print(data_adult[data_adult['continent'] == 1].loc[:,['country','continent']])
# print(data_adult.groupby('continent').agg({'continent':'count'}))
# print(data_adult)
# print(data_adult.groupby('country').agg({'country':'count'}))


compression_opts = dict(method= 'zip', archive_name = 'out.csv')
data_adult.to_csv('out.zip', index=False,
          compression=compression_opts)






