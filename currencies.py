from alpha_vantage.foreignexchange import ForeignExchange

class CurrencyPair:
    """
    Currency class
    """

    def __init__(self,domcur,forcur):
        """
        Parameters
        ----------
        domcur : str
            Currency code (e.g. USD, EUR) of domestic currency
        forcur : str
            Currency code (e.g. USD, EUR, YEN etc.) of foreign currency
        """

        # alpha vantage
        key = input('API key: ')
        fc = ForeignExchange(key, output_format='pandas')

        # pull spot prices
        cur_dat = fc.get_currency_exchange_rate(domcur,forcur)
        E0 = float(cur_dat[0].loc[cur_dat[0].index[0],'5. Exchange Rate'])

        self.attr_dict = {
            'domcur' : domcur,
            'forcur' : forcur,
            'date' : cur_dat,
            'E0' : E0
        }
        
    def pricing(self,rD,rF):
        # TODO: find good API to pull rD and rF
        """
        Pricing method

        Parameters
        ----------
        rD : float
            Domestic risk-free rate
        rF : float
            Foreign risk-free rate

        """
        setup = 'On {date}, a {forcur} cost {E0:.4f} {domcur}.'
        question = 'What should the forward price be?'

        self.attr_dict['K0'] = self.attr_dict['E0']*(1.+rD)/(1.+rF)

        answer = 'The forward price should be {K0} {domcur}.'
        text = text.format(**self.attr_dict)

        return text

    def arbitrage(self):
        """
        Arbitrage method
        """

        over_priced = (self.K0_act > self.E0*(1.+self.rD)/(1.+self.rF))

        if over_priced:
            borcur = self.forcur
            invcur = self.domcur
            invamt0 = 1.
        else:
            borcur = self.domcur
            invcur = self.forcur
            invamt1 = 1.

        setup = 'On {date}, a {forcur} cost {E0:.4f} {domcur}.'

        question = 'Is the forward over- or under-priced?'
        question += 'How would you exploit this mis-pricing?'
        question += 'How much do you expect to make?'
        question += 'How much does your portfolio cost?\n\n'

        answer = 'Today,'
        answer += '1. Borrow 1 {borcur}'
        answer += '2. buy {invamt0} {invcur}'
        answer += '3. buy {invamt0} {invcur} of {invcur}-denominated risk-free bonds'
        answer += '4. {pos} a forward with price {K}'
        answer += 'In one year,'
        answer += '1. Collect {invamt1} {invcur} from {invcur}-denominated risk-free bonds'
        answer += '2. Use the forward to {pos} your {invcur} and receive 1.2866 {borcur}'
        answer += '3. Repay loan balance of 1.003 {borcur}.'
        answer += '4. Keep the rest.'

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text
