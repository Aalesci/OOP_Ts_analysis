import requests
import key as ks
from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Return_OOP as roop
import Backtest_OOP as boop

print(range(0,16,1))

sm1 = range(2, 20, 1)
sm2 = range(2, 20, 1)

for i in sm2:  
    for s in sm1: 
        if i > s:  
            print(s, i)

'''
noise = [0.01 ,0.02 , -0.01]
name = ['uno', 'due', 'tre']
name2 = ['pip', 'pop', 'pho']
my_s = pd.Series(noise, name )
my_s2 = pd.Series(noise, name2 )
s = my_s.append(my_s2,ignore_index = False)  
print(s)
'''

Tiker = 'BTCBUSD'
time = '1d'
start_date = '1-01-2022'
end_date = '1-10-2022'

df = boop.get_df_for_analisi(Tiker, time, start_date, end_date)

df['pct_change'] = df['Close'].pct_change()
df.dropna(inplace=True)
#s = pd.Series(df['pct_change'], index= df.index )
#print(s)
#print(df['Close'])

import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

fig, ax1 = plt.subplots()
ax1.plot(df.index, df['Close'])
# Rotate and align the tick labels so they look better.
fig.autofmt_xdate()
#dtFmt = mdates.DateFormatter('%Y-%m-%d') # define the formatting
#ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
#ax.xaxis.set_major_formatter(dtFmt)
# Use a more precise date string for the x axis locations in the toolbar.
ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
ax1.set_title('fig.autofmt_xdate fixes the labels')
#plt.show()

df = boop.synbol_and_trade_fee()



