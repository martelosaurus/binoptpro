import random
from stocks import Stock

class Forward(Stock):
    """
    Forward class
    """

    def __init__(self,ticker,T):
        super().__init__(ticker)

        K = self.S[0]*(1.+self.rF)**T
        K_act = random.uniform(.8*K,1.2*K)

        self.attr_dict = {
            'T' : T,
            'tick' : self.tick,
            'date' : self.date[0],
            'S0' : self.S[0],
            'rF' : self.rF,
            'K' : K,
            'K_act' : K_act,
            'l' : self.S[0]-K_act, # long forward payoff
            's' : K_act-self.S[0]  # short forward payoff
        }

    def payoffs(self,buy=True,answer=True):
        """
        Returns a forward pricing question

        Parameters
        ----------
        buy : boolean
            If True, then long, else short
        answer : boolean
            If True, then reports the answer
        """

        if buy: # long
            your_payoff = self.attr_dict['l']
            self.attr_dict['long_short'] = 'long'
        else: # short
            your_payoff = self.attr_dict['s']
            self.attr_dict['long_short'] = 'short'

        setup = 'On {date}, {tick} traded for {S0:.4f} USD. '
        setup += 'Suppose you were {long_short} a {K_act:.4f} USD forward that expired on {date}. '  

        question = 'What was your payoff?\n\n' 

        answer = 'Your payoff was ' + format(your_payoff,'.4f') + ' USD.'

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text

    # TODO: document
    def pricing(self,call=True,buy=True):
        """
        Returns an option pricing question

        Parameters
        ----------
        call : boolean
            If True, then call option, else put option
        buy : boolean
            If True, then long, else short
        answer : boolean
            If True, then reports the answer

        """

        setup = 'On {date}, {tick} traded for {S0:.4f} USD. The annual risk-free rate is {rF:.4f}. '

        question = 'What is the forward price of a {T}-year forward?\n\n' 

        answer = 'The forward price is {K:.4f} USD.'

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text

    def arbitrage(self):
        """
        Option arbitrage problem
        """
        pass
