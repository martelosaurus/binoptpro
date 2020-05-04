from options import BinomialOption
from forwards import Forward

f_exam = open('exam.txt','w')

TSLA_opt = BinomialOption('TSLA')
TSLA_for = Forward('TSLA',10)

for b in [True,False]:
    f_exam.writelines(TSLA_for.payoffs(buy=b) + '\n\n')
    f_exam.writelines(TSLA_for.pricing(buy=b) + '\n\n')
    for c in [True,False]:
        f_exam.writelines(TSLA_opt.payoffs(call=c,buy=b) + '\n\n')
        f_exam.writelines(TSLA_opt.pricing(call=c,buy=b) + '\n\n')

f_exam.close()
