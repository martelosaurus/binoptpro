class Option(Security):
    """Option class. Currently only setup for stock options."""

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
            'Dc' : Dc,
            'Bc' : Bc, 
            'C0' : C0,
            'Dp' : Dp,
            'Bp' : Bp,
            'P0' : P0,
            'lc' : max(S[0]-K,0), # long call payoff
            'sc' : min(K-S[0],0), # short call payoff
            'lp' : max(K-S[0],0), # long put payoff
            'sp' : min(S[0]-K,0)  # short put payoff
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

        setup = '\\noindent On {date}, {tick} traded for {S0} USD. '
        setup += 'In one month, {tick} can either go up to {Su} USD or down to {Sd} USD. '
        setup += 'Suppose that on {date}, you went {long_short} a {K} USD {call_put}. '

        question = 'What was the option premium that you paid or received? '
        question += 'How would you hedge your position?\n\n\\vspace{{9pt}}'

        D = self.attr_dict['Dc'] if call else self.attr_dict['Dp']
        B = self.attr_dict['Bc'] if call else self.attr_dict['Bp']

        answer = '\n\n\\noindent\\textbf{{Solution.}} '
        sub = '_{{c}}' if call else '_{{p}}'
        answer += '$\\Delta' + sub + '$ is ' + str(D) + ', '
        answer += '$B' + sub + '$ is ' + str(B) + ' USD, and so '

        if call:
            answer += '$C_{{0}}$ is ' + str(self.attr_dict['C0']) + ' USD. '
        else: # if put
            answer += '$P_{{0}}$ is ' + str(self.attr_dict['P0']) + ' USD. '

        answer += 'To hedge your position, '
        if call:
            answer += 'you should go {short_long} ' + str(D) + ' shares of {tick} and '  
            answer += '{long_short} ' + str(B) + ' USD in the risk-free asset.' 
        else:
            answer += 'you should go {long_short} ' + str(D) + ' shares of {tick} and '  
            answer += '{short_long} ' + str(B) + ' USD in the risk-free asset.' 

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
