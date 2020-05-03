class Currency(Security):
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

        self.r_f
        
    def pricing(self):
            
        return text
            

    def arbitrage(self):

        over_priced = (self.K0_act > self.E0*(1.+self.rD)/(1.+self.rF))

        if over_priced:
            borcur = self.forcur
            invcur = self.domcur
        else:
            borcur = self.domcur
            invcur = self.forcur

        question = 'Is the forward over- or under-priced?'
        question += 'How would you exploit this mis-pricing?'
        question += 'How much do you expect to make?'
        question += 'How much does your portfolio cost?\n\n'

        answer = 'Today,'
        answer += '1. Borrow 1 {borcur}'
        answer += '2. buy .9174 {invcur}'
        answer += '3. buy .9174 {invcur} of {invcur}-denominated risk-free bonds'
        answer += '4. {pos} a forward with price {K}'
        answer += 'In one year,'
        answer += '1. Collect .9119 {invcur} from {invcur}-denominated risk-free bonds'
        answer += '2. Use the forward to {pos} your {invcur} and receive 1.2866 {borcur}'
        answer += '3. Repay loan balance of 1.003 {borcur}.'
        answer += '4. Keep the rest.'

        text = setup + question + answer
        text = text.format(**self.attr_dict)

        return text
