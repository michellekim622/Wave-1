import math

princ_acc = input(" please enter the principial amount : ")

princ_acc = float(princ_acc)

one_year_amount = princ_acc+princ_acc*4/100
two_year_amount = one_year_amount+one_year_amount*4/100
three_year_amount = two_year_amount+two_year_amount*4/100

# calculate the compound interest for each one, two and three year
print("future compound interest for one year amount will be %.2f" %one_year_amount)
print("future compound interest for two year amount will be %.2f" %two_year_amount)
print("future compound interest for three year amount will be %.2f" %three_year_amount)
