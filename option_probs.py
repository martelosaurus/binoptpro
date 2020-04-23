import datetime, random
import pandas as pd
import tkinter as tk
from alpha_vantage.timeseries import TimeSeries
from tkinter import Tk
key = input('API key: ')
ts = TimeSeries(key, output_format='pandas')

tickers = ['AAPL','DIS','MSFT','NKE']
rF = .001 # risk-free rate

def clipboardz(text)
    """Loads 'text' into clipboard (thanks to someone on SO)"""
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update() 
    r.destroy()

class Stock:

    def __init__(self,date,S0):

        self.date = date

        self.S0
        self.S1

        
        self.Su = Su
        self.Sd = Sd
        self.K = random.uniform(self.Sd,self.Su) 
        
        self.call_Delta = 
        self.call_Beta = 

        self.put_Delta = 
        self.put_Beta = 

    def payoff(self,call=True,buy=True)
        """
        Returns an option pricing question

        Parameters
        ----------

        """
        line1 = 'On {date}, {ticker} traded for '
        clipboardz()

    def pricing(self,call=True,buy=True)
        """
        Returns an option pricing question

        Parameters
        ----------

        """
        pass

    def hedging(self,call=True,buy=True) 
        """
        Returns an option pricing question

        Parameters
        ----------

        """
        pass


stocks = []
for ticker in tickers:
    tick_data, _ = ts.get_monthly_adjusted(symbol=ticker)
    tick_data = tick_data.sort_index()
    tick_data = tick_data[-3:-1] # pull the last two observations
    stocks.append(Stock(tick_data[-1].index,Su,Sd))

