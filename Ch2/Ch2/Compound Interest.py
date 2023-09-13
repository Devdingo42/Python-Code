#Compound Interest
#When a bank account pays compound interest, it pays interest not only on the principal
#amount that was deposited into the account, but also on the interest that has accumulated
#over time. Suppose you want to deposit some money into a savings account, and let the
#account earn compound interest for a certain number of years. The formula for calculating
#the balance of the account after a specified number of years is:

#Origianl deposit
Original_Deposited_P = float(input('Enter the principal amount that was originally deposited into the account: '))

#Annual interest rate
Interest_rate_R = float(input('Enter The annual interest rate paid by the account as a decimal: '))

#Interest is compounded
Times_per_year = float(input('Enter the number of times per year that the interest is compounded: '))

#Years
Number_Years = float(input('Enter the number of years the account will be left to earn interest: '))

#Amount of Money
Amount_of_Money = (Original_Deposited_P * ((1 + (Interest_rate_R / Times_per_year)) ** (Times_per_year * Number_Years)))

print('The amount of money that will be in the account after', Number_Years, 'years is,', Amount_of_Money, '$')