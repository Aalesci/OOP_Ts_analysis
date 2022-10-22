import requests
import key as ks
from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Return_OOP as roop

# Insert API and Secret key in quotation marks
client = Client(ks.api_key, ks.api_secret)

def synbol_and_trade_fee():
    # funzione che ritorna tutti i tiker.
    trade_fee = client.get_trade_fee()
    df = pd.DataFrame(trade_fee, columns=[
                      'symbol', 'makerCommission', 'takerCommission'])
    df_tiker = df['symbol']
    return df_tiker


def get_df_for_analisi(Tiker, time, start_date, end_date):
    # return df of a tiker
    df_strings = client.get_historical_klines(Tiker, time, start_date, end_date)
    for df_string in df_strings:
        del df_string[7:]
    df = pd.DataFrame(df_strings, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'QA volume'])
    df.set_index('Date', inplace=True)
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype({"Open": float, "High": float, "Low": float,"Close": float, "Volume": float, "QA volume": float})
    return df


class Backtest:

    def __init__(self, symbol, df, time, start_date , end_date, SM1, SM2 ):
        self.symbol = symbol
        self.df = df 
        self.start_date = start_date
        self.end_date = end_date
        self.time = time
        self.SM1 = SM1
        self.SM2 = SM2
        if self.SM2 <= self.SM1: 
            print('Strategy not consistent')
        if not self.df.empty:
            self.strategy_indicators()
            self.signals()
            self.filter()
            if len(self.ar_buy) >= 1 and len(self.ar_sell) >= 1:
                self.analysis()
        else:
            print('No data for : ' + self.symbol)
        #self.result = self.desc_data.append(self.strategy,ignore_index = False)
        

    def strategy_indicators(self):
        self.strategy = pd.Series([self.SM1, self.SM2],['N.Periods SM1','N.Periods SM2']) 
        self.df['SMA1'] = self.df['Close'].rolling(self.SM1).mean()
        self.df['SMA2'] = self.df['Close'].rolling(self.SM2).mean()
        self.df.dropna(inplace=True)  # Implemet: Delete just the unnecessary row.


    def signals(self):
        self.df['Signal'] = np.where(
            self.df['SMA1'] > self.df['SMA2'], 'Buy', 'Sell')
        self.df.Signal = self.df.Signal.shift()
        self.df.dropna(inplace=True)

    def filter(self):
        position = False
        buydate, selldate = [], []
        for index, row in self.df.iterrows():
            if not position and row['Signal'] == 'Buy':
                position = True
                buydate.append(index)
            if position and row['Signal'] == 'Sell':
                position = False
                selldate.append(index)

        self.ar_buy = self.df.loc[buydate].Close
        self.ar_sell = self.df.loc[selldate].Close

        print('Ar buy')
        print(self.ar_buy)
        print('Ar sell')
        print(self.ar_sell)

        if len(self.ar_buy) >= 1 and len(self.ar_sell) >= 1:   
            if self.ar_buy.index[-1] > self.ar_sell.index[-1]:
                 self.ar_buy = self.ar_buy[:-1]

            self.strategy_returns = pd.Series((self.ar_sell.values - self.ar_buy.values ) / self.ar_buy.values)


    def analysis(self):
        if len(self.ar_buy) >= 1 and len(self.ar_sell) >= 1:
            self.object_return = roop.Return( self.strategy_returns, self.symbol, self.time, self.start_date, self.end_date)
            self.desc_data = self.object_return.ret 
        else: 
            noise = np.random.normal(0,1,50)
            my_s = pd.Series(noise)
            self.object_return = roop.Return( my_s, self.symbol, self.time, self.start_date, self.end_date)
            self.desc_data =  self.object_return.ret 



###### DATA FOR INTERNAL TEST #######

# SETTING for get_df_for_analisi
#Tikers = [ 'BTCBUSD', 'ETHBUSD', 'LTCBUSD', 'SOLBUSD' ]
'''
Tiker = 'BTCBUSD'
time = '30m'
start_date = '1-01-2022'
end_date = '1-03-2022'
'''

#df = get_df_for_analisi(Tiker, time, start_date, end_date)
#istance = Backtest(Tiker, df , time, start_date, end_date, 6, 10)
#print(istance.result)


# print(data_frame) 
# print(istance.df)
# print(istance.ar_buy)
# print(istance.ar_sell)
# print(istance.strategy_returns)
# print(istance.cumulative_profit)
# print(istance.accuracy)
# print( get_df_for_analisi(Tiker, time ,start_date, end_date).head() )
# Apply the default theme
