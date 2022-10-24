import requests
import key as ks
from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Return_OOP as roop
import Backtest_OOP as boop


#Tikers = [ 'BTCBUSD', 'ETHBUSD', 'LTCBUSD', 'SOLBUSD' ]
#for Tiker in Tikers:
#Tiker = 'BTCBUSD'
#to_excell(Tiker, time, start_date, end_date)

Tiker = 'BTCBUSD'
time = '1h'
start_date = '1-01-2022'  #Month #Day  #Years 
end_date = '1-2-2022'     #Month #Day  #Years


#Algoritmo per il passaggio dei dati 
def to_excell(Tiker, time, start_date, end_date): 
    df = boop.get_df_for_analisi(Tiker, time, start_date, end_date)
    #print(df)
    data_frame = pd.DataFrame()

    #Algoritmo per il passaggio dei dati 
    sm1 = range(2, 10, 1)
    sm2 = range(2, 10, 1)

    for i in sm2:  
        for s in sm1: 
            if i > s:  
                print('Sma ' + str(s) + str(i) )
                istance = boop.Backtest(Tiker, df , time, start_date, end_date, s, i)
                data_frame = data_frame.append(istance.desc_data, ignore_index=True) #non è più desc data

    sheet_name = str(Tiker +'_'+ time +'_'+ start_date +'_'+ end_date + '.xlsx')
    excel_name = str(Tiker +'_'+ time)
    data_frame.to_excel(sheet_name ,sheet_name= excel_name)



to_excell(Tiker, time, start_date, end_date)