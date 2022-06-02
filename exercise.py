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
data_adult = data_adult[data_adult['country'] != '?']
# print(len(data_adult[data_adult['country']=='?']))

#age checked
plt.plot(data_adult['age'])
# plt.show()

print(data_adult['employment'].unique())
print(len(data_adult[data_adult['employment']=='?']))
print(data_adult['education'].unique())
print(data_adult['civil status history'].unique())
print(data_adult['profession'].unique())
print(data_adult['relationship'].unique())
print(data_adult['skin colour'].unique())
print(data_adult['sex'].unique())
print(data_adult['working time hours/week'].max())
print(data_adult['country'].unique())
print(data_adult['annual income'].unique())

bins = [0, 10, 30, 50, 99]
labels = ['odd job','part-time job','full-time job', 'workaholism']
data_adult['Work time categories'] = pd.cut(data_adult['working time hours/week'], bins, labels =labels)
print(data_adult)
# print(len(data_adult[data_adult['Work time categories'] == 'workaholism']))
print(data_adult.groupby('Work time categories').agg({'Work time categories': 'count', 'age':'mean'}))

# print(data_adult.info())

