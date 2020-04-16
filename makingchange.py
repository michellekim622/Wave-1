import math

# making change
change=int(input( 'Please enter an amount :' ))

# toonie used
if (change// 200) != 0 :
    print(change//200, "toonies")
change=change%200

#loonies used
if (change// 100) != 0 :
    print(change//100, "loonies")
change=change%100

# quaters used
if (change// 25) != 0 :
    print(change//25, "quaters")
change=change%25

# dimes used
if (change// 10) != 0 :
    print(change//10, "dimes")
change=change%10

# nickels used
if (change// 5) != 0 :
    print(change//5, "nickels")
change=change%5

# pennies used
if (change// 1) != 0 :
    print(change//1, "pennies")
change=change%1
