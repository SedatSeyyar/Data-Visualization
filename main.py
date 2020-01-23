# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:10:20 2020

@author: Sedat
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("ist-temiz-su-mik.xlsx")

X=data["Ay"]

plt.subplots(2,1, figsize=(20, 10))
plt.subplot(2, 1, 1)
plt.plot(X, data[2015], label='2015')
plt.plot(X, data[2016], label='2016')
plt.plot(X, data[2017], label='2017')
plt.plot(X, data[2018], label='2018')
plt.plot(X, data[2019], label='2019', color='purple',lw=2)

plt.legend(loc='lower left',ncol=3)
plt.ylabel('Temiz Su Miktarı')
plt.title("İstanbul'a Verilen Temiz Su Miktarları 2009-19")
plt.subplot(2, 1, 2)

plt.plot(X, data[2009], label='2009')
plt.plot(X, data[2010], label='2010')
plt.plot(X, data[2011], label='2011')
plt.plot(X, data[2012], label='2012')
plt.plot(X, data[2013], label='2013')
plt.plot(X, data[2014], label='2014')
plt.xlabel('Aylar')
plt.ylabel('Temiz Su Miktarı')
plt.legend(loc='upper left',ncol=3)
plt.show()

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
          'purple', 'orange', 'red']
labels = data.columns[1:12]
sizes = data.iloc[:,1:12].sum()
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05)

fig1, ax1 = plt.subplots(figsize=(10,10))
ax1.pie(sizes, explode=explode, labels=labels,colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=200)

plt.title("İstanbul'a Verilen Yıllık Temiz Su Miktarları 2009-19")
plt.show()