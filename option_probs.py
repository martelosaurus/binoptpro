"""
Security class, stock/bond/currency classes, and forward/option classes. Each class has payoff,
pricing, and arbitrage methods
"""
import datetime, random
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# alpha vantage
key = input('API key: ')
ts = TimeSeries(key, output_format='pandas')

class Security:
    """
    Security class
    """

    def __init__(self,ticker,rF=.001):

        # pull spot prices
        tick_data, _ = ts.get_monthly_adjusted(symbol=ticker)
        tick_data = tick_data.sort_index()
        S = tick_data.loc[tick_data.index[-3:-1],'5. adjusted close']

        # up/down returns
        rS_up = .1
        rS_dn = -.1

        # TODO: think about other ways to select Su, Sd, K
        Su = (1.+rS_up)*S[0]
        Sd = (1.+rS_dn)*S[0]

class Portfolio:
    """
    Portfolio class
    """
    def __init__(self,securities):
        """
        securities : list (of securities)
            List of security objects
        """
        self.securities = securities

    def plot(self):
        """
        Plots the portfolio in risk-return space
        """
        pass

