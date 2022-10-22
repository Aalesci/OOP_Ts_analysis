from operator import index
from statistics import variance
import statistics

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#noise = np.random.normal(0,1,4)
#noise = [0.01 ,0.02 , -0.01, 1.03]
#my_s = pd.Series(noise)
#print(my_s)

class Return:

    def __init__(self, series, symbol ,time, start , end, graphics = False ): 
        self.series = series
        self.symbol = symbol 
        self.time = time 
        self.start = start 
        self.end  = end 
        #self.stat = pd.Series(self.statistic(), self.index_statistic) 
        #self.anal = pd.Series(self.analysis(), self.index_anaysis) 
        self.ret  = pd.Series(self.basic() + self.analysis() + self.statistic() ,self.index_basic + self.index_anaysis + self.index_statistic) 
        self.graphics = graphics
        if  self.graphics == True: 
            self.plot_graphics()

    def basic(self): 
        self.index_basic = ['symbol', 'Time', ] #'N.Periods SM1','N.Periods SM2']
        info = [self.symbol ,self.time ] #self.SM1 , self.SM2 ] 
        return info 

    def analysis(self):
        self.index_anaysis =['Start Trade', 'End Trade' ,'Trades N.','Accuracy %', 'Cumulative Return ','VaR5%', 'VaR10%'] 
        self.series.sort_values()

        cont = 0  
        for index, value in self.series.items():
           if value >= 0: 
            cont = cont + 1
        print('Cont // e self series cont:'+ str(cont) + str(self.series.count()))
        accuracy = (cont / self.series.count()) * 100

        VaR_95 = self.series.quantile(0.05).round(4)
        VaR_90 = self.series.quantile(0.1).round(4)
        analysis = [self.start, self.end, self.series.count(), accuracy , (self.series + 1).prod() - 1, VaR_95 , VaR_90]
        return analysis

    def statistic(self):
        self.index_statistic  = [ 'Maximum', 'Minimum','Mean', 'Varinace', 'StandardDev' , 'Kurtosis', 'Skewness']
        statistic = [self.series.max(),self.series.min(),self.series.mean(),self.series.var(),self.series.std(), 
        self.series.kurtosis(), self.series.skew() ]
        return statistic
        
    '''
    def strategy(self): 
        self.index_strategy = ['N.Periods SM1','N.Periods SM2']
        strategy = [self.SM1, self.SM1]
        return strategy 
    '''

    def plot_graphics(self): 
        fig, ax = plt.subplots()
        mu = self.series.mean()
        self.series.plot( kind='hist', ax=ax ,label = 'N. bands')
        self.series.plot( kind='kde',grid=True, ax=ax, secondary_y=True )
        ax.plot([mu,mu],[0,10], label='Mean '+ "{}".format(round(mu, 3)), color = 'r' )
        ax.set_title(self.symbol +' - '+ self.start +' ' +self.end  )
        ax.legend()
        fig.tight_layout()
        plt.show()




#istance = Return(my_s, 'symbol' ,'1 Ora',  'SM1' , 'SM2','start', 'end' , graphics = False )
#print(istance.ret)
#print(istance.series)