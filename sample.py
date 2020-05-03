f_prac = open('prac.txt','w')
f_exam = open('exam.txt','w')

# APT
IBM = Stock('IBM')
AMD = Stock('AMD')

if False:

    # forwards I
    IBM = Forward('IBM')
    AMD = Forward('AMD')

    # forwards II
    USD_EUR = Currency('USD','EUR')
    USD_YEN = Currency('USD','YEN')

    # options
    IBM = Option('IBM')
    AMD = Option('AMD')

    # option
    f_prac.writelines(IBM.pricing() + '\n\n')
    f_prac.writelines(IBM.pricing() + '\n\n')

f_prac.close()
f_exam.close()
