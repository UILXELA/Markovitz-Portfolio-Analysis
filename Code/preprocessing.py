import pandas as pd
import numpy as np
import scipy.io as sp

names = ['time', 'val']
df = pd.read_csv("market.csv", names = names)
df = df.dropna(how='any')
df['time'] = pd.to_datetime(df['time'], format='%m/%d/%Y') 
df = df.iloc[:,0:2]
df['return'] = df[1:].apply(lambda row: (df['val'][row.name]-df['val'][row.name-1])/df['val'][row.name-1]*100, axis=1)
df = df.set_index('time')
df = df['2016-01-01':'2017-01-01']
df = df.drop('val',axis = 1)
print(df)

sp.savemat('sp500_2016.mat', {'struct':df.to_dict("list")})



def clean(returns):
    for i in range(0, returns.shape[0]):
        if returns[i] == -99 or returns[i] == -999:
            return (returns[i-1]+returns[i+1])/2
        
df2 = pd.read_csv('FF48.csv')
df2['time'] = pd.to_datetime(df2['time'], format='%Y%m%d')
df2.apply(clean)
print(df2[df2<-99].dropna(how='any'))                                   #check validity of data
df2 = df2.set_index('time')
df2 = df2['2016-01-01':'2017-01-01']
sp.savemat('FF48_2016.mat', {'struct':df2.to_dict("list")})


print(df2)


