import requests
import key as ks
from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import Return_OOP as roop
import Backtest_OOP as boop 

class Bechmark(): 

    def __init__(self, symbol, df, time, start_date, end_date, graphics = False ):
        self.symbol = symbol
        self.df = df 
        self.start_date = start_date
        self.end_date = end_date
        self.time = time 
        self.bench()
        if graphics == True: 
            self.graphics()

    def bench(self): 
        #Get return series #use it with return_OOP 
        self.df['pct_change'] = self.df['Close'].pct_change()
        self.df.dropna(inplace=True)
        self.returns = pd.Series(self.df['pct_change'], index= self.df.index )
        self.object_return = roop.Return( self.returns, self.symbol, self.time, self.start_date, self.end_date)
        self.desc_data = self.object_return.ret 

    def graphics(self): 

        #fig, (ax1, ax2) = plt.subplots(2, 1)
        # make a little extra space between the subplots
        #fig.subplots_adjust(hspace=0.5)

        fig, ax1 = plt.subplots()
        fig.autofmt_xdate()
        ax1.plot(df.index.date, self.df['Close'])
        ax1.set_title(self.symbol + self.time +' '+ self.start_date +' ' +self.end_date )
        #if self.time == '1d':  
        #    ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        #else:
        ax1.fmt_xdata = mdates.DateFormatter('%H:%M')
        plt.show()
        


'''
Tiker = 'BTCEUR'
time = '1d'
start_date = '1-01-2022'
end_date = '1-1-2022'

df = boop.get_df_for_analisi(Tiker, time, start_date, end_date)

istance = Bechmark( Tiker, df, time, start_date, end_date, graphics = True )
#print(istance.df)
'''