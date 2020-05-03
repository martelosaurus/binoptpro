import random
from stocks import Stock

class BinomialOption(Stock):
    """Option class. Currently only setup for stock options."""

    def __init__(self,ticker):
        super().__init__(ticker)

        K  = random.uniform(self.Sd,self.Su)

        # call
        Dc = (self.Su-K)/(self.Su-self.Sd)
        Bc = Dc*self.Sd/(1.+self.rF)
        C0 = Dc*self.S[0]-Bc

        # put 
        Dp = (K-self.Sd)/(self.Su-self.Sd)
        Bp = Dp*self.Su/(1.+self.rF)
        P0 = Bp-Dp*self.S[0]

        self.attr_dict = {
            'tick' : self.tick,
            'date' : self.date,
            'S0' : self.S[0],
            'S1' : self.S[1],
            'Su' : self.Su,
            'Sd' : self.Sd,
            'K'  : K, 
            'rF' : self.rF,
            'Dc' : Dc,
            'Bc' : Bc, 
            'C0' : C0,
            'Dp' : Dp,
            'Bp' : Bp,
            'P0' : P0,
            'lc' : max(self.S[0]-K,0), # long call payoff
            'sc' : min(K-self.S[0],0), # short call payoff
            'lp' : max(K-self.S[0],0), # long put payoff
            'sp' : min(self.S[0]-K,0)  # short put payoff
        }

    # TODO: document
    def payoffs(self,call=True,buy=True,answer=True):
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

        self.attr_dict['long_short'] = 'long' if buy else 'short'
        self.attr_dict['short_long'] = 'short' if buy else 'long'
        self.attr_dict['call_put'] = 'call' if call else 'put'

        if call:
            long_payoff = self.attr_dict['lc']
            if buy: # long
                your_payoff = self.attr_dict['lc']
            else: # short
                your_payoff = self.attr_dict['sc']
        else: # if put
            long_payoff = self.attr_dict['lp']
            if buy: # long
                your_payoff = self.attr_dict['lp']
            else: # short
                your_payoff = self.attr_dict['sp']
                
        lectpath = '/home/jordan/Projects/investments-lectures/L61_OptionsI/'

        setup = '\\noindent On {date}, {tick} traded for {S0} USD. '
        setup += 'Suppose you were {long_short} a {K} USD {call_put} that expired on {date}. '  

        question = 'Was the option in, at, or out-of-the-money? '
        question += 'Was the option exercised? '
        question += 'What was your payoff at expiration?\n\n\\vspace{{9pt}} '

        answer = '\n\n\\textbf{{Solution.}}'
        answer += 'The option was ' + ('in-' if long_payoff > 0 else 'out-of-') + 'the-money, ' 
        answer += 'so it was ' + ('exericed.' if long_payoff > 0 else 'not exercised. ')
        answer += 'Your payoff was ' + str(your_payoff) + ' USD.'

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

        self.attr_dict['long_short'] = 'long' if buy else 'short'
        self.attr_dict['short_long'] = 'short' if buy else 'long'
        self.attr_dict['call_put'] = 'call' if call else 'put'

        setup = '\\noindent On {date}, {tick} traded for {S0:.4f} USD. '
        setup += 'In one month, {tick} can either go up to {Su:.4f} USD or down to {Sd:.4f} USD. '
        setup += 'Suppose that on {date}, you went {long_short} a {K:.4f} USD {call_put}. '

        question = 'What was the option premium that you paid or received? '
        question += 'How would you hedge your position?\n\n\\vspace{{9pt}}'

        D = self.attr_dict['Dc'] if call else self.attr_dict['Dp']
        B = self.attr_dict['Bc'] if call else self.attr_dict['Bp']

        answer = '\n\n\\noindent\\textbf{{Solution.}} '
        sub = '_{{c}}' if call else '_{{p}}'
        answer += '$\\Delta' + sub + '$ is ' + format(D,'.4f') + ', '
        answer += '$B' + sub + '$ is ' + format(B,'.4f') + ' USD, and so '

        if call:
            answer += '$C_{{0}}$ is ' + format(self.attr_dict['C0'],'.4f') + ' USD. '
        else: # if put
            answer += '$P_{{0}}$ is ' + format(self.attr_dict['P0'],'.4f') + ' USD. '

        answer += 'To hedge your position, '
        if call:
            answer += 'you should go {short_long} ' + format(D,'.4f') + ' shares of {tick} and '  
            answer += '{long_short} ' + format(B,'.4f') + ' USD in the risk-free asset.' 
        else:
            answer += 'you should go {long_short} ' + format(D,'.4f') + ' shares of {tick} and '  
            answer += '{short_long} ' + format(B,'.4f') + ' USD in the risk-free asset.' 

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text

    def arbitrage(self):
        """
        Option arbitrage problem
        """
        pass

    def plot(self):
        """
        Option payoff plot
        """
        pass
