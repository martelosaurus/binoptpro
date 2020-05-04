import pandas as pd
from alpha_vantage.timeseries import TimeSeries

class Stock:
    """
    Stock class
    """

    def __init__(self,ticker):
        super().__init__()

        # TODO: don't hardcode this
        self.rF = .001

        # alpha vantage
        key = input('API key: ')
        ts = TimeSeries(key, output_format='pandas')

        # pull spot prices
        tick_data, _ = ts.get_monthly_adjusted(symbol=ticker)
        tick_data = tick_data.sort_index()
        self.S = tick_data.loc[tick_data.index[-3:-1],'5. adjusted close']

        # up/down returns
        rS_up = .1
        rS_dn = -.1

        # TODO: think about other ways to select Su, Sd, K
        self.Su = (1.+rS_up)*self.S[0]
        self.Sd = (1.+rS_dn)*self.S[0]

        # basic info
        self.tick = ticker
        self.date = tick_data.index[-2].isoformat()[:10],

    def plot(self):
        """Plots stock price and dividends."""
        pass

    def arbitrage(self):
        """APT problem."""

        setup = '\\noindent On {date}, {tick} traded for {S0:.4f} USD. '

        question = 'Is the stock over- or under-priced?'
        question += 'How would you exploit this mispricing?'
        question += 'How much do you expect to make?'
        question += 'How much does your portfolio cost?\n\n\\vspace{{9pt}}'

        #answer = 'The stock is ' + overunder + ' priced.' 
        #answer += 'In order to exploit this mis-pricing, ' + step1 + step2 + step3. 
        answer += 'In one month, you expect to make'
        answer += 'Your portfolio does not cost anything.'

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text
