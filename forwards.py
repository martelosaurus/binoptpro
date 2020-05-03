class Forward(Security):
    """
    Forward class
    """

    def __init__(self):
        
        super().__init__(ticker):

        K  = random.uniform(Sd,Su)

        # call
        Dc = (Su-K)/(Su-Sd)
        Bc = Dc*Sd/(1.+rF)
        C0 = Dc*S[0]-Bc

        # put 
        Dp = (K-Sd)/(Su-Sd)
        Bp = Dp*Su/(1.+rF)
        P0 = Bp-Dp*S[0]

        self.attr_dict = {
            'tick' : ticker,
            'date' : tick_data.index[-2].isoformat()[:10],
            'S0' : S[0],
            'S1' : S[1],
            'Su' : Su,
            'Sd' : Sd,
            'K'  : K, 
            'rF' : rF,
            'l' : S[0]-K, # long forward payoff
            's' : K-S[0]  # short forward payoff
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
            your_payoff = self.attr_dict['lc']
        else: # short
            your_payoff = self.attr_dict['sc']

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

    def arbitrage(self):
        """
        Option arbitrage problem
        """
        pass
