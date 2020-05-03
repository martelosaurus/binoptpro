"""
Security class, stock/bond/currency classes, and forward/option classes. Each class has payoff,
pricing, and arbitrage methods
"""
import datetime, random
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

class Security:
    """
    Security class
    """

    def __init__(self,ticker):

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

