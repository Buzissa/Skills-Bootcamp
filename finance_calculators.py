# This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

user = input("What is your name?")
print("Hello " + user)

import math

print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")

print ("")
calculator = input ("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculator = calculator.lower()     # How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, BOND’, ‘Investment’, ‘INVESTMENT' will all be recognised as valid entries.

print("")

if calculator != "investment" and calculator != "bond":
    print ("Please run the program again and insert either 'investment' or 'bond'")     # Error message will be displayed if the input is neither "investment" nor "bond"

elif calculator == "investment":     # If the user selects the investment calculator, she/he will be asked for the following information: deposit amount, interest rate, years of investment and interest type
    
    deposit = int (input ("What is the amount of your deposit in GBP? "))
    rate = int (input ("What is the interest rate? Please insert only the number. e.g. insert only '8' if interest rate is 8% : "))
    years = int (input ("How many years are you planning on investing? "))
   
    interest = input ("Would your prefer simple or compound interest? Please insert 'simple' or 'compound' for your preferred option: ")
    interest = interest.lower()     # How the user capitalises their selection should not affect how the program proceeds

    while interest != "simple" and interest != "compound":     # Ask the user to reinsert an input until it is either 'simple' or 'compound'
        interest = input ("Please insert either 'simple' or 'compound' ")
        interest = interest.lower()
    
    if interest == "simple":     # If the user selects simple interest, program will calculate earnings and display that amount
        earnings = deposit * (1 + rate/100 * years)
        print("")
        print (f"At {rate}% interest rate, you would turn £{deposit} into £{round(earnings,2)} after {years} years")

    if interest == "compound":     # If the user selects compound interest, program will calculate earnings and display that amount
        earnings = deposit * math.pow((1+rate/100),years)
        print("")
        print (f"At {rate}% interest rate, you would turn £{deposit} into £{round(earnings,2)} after {years} years")

elif calculator == "bond":     # If the user selects the bond calculator, she/he will be asked for the following information: house value, interest rate, time to repay.

    house = int(input ("What is the present value of your house, in GBP? "))
    rate = int(input ("What is the interest rate? Please insert only the number. e.g. insert only '8' if interest rate is 8% "))
    months = int(input ("How many months do you plan to take to repay the bond? "))

    repayment = (rate/100/12 * house) / (1 - (1 + rate/100/12)**(-months))     # Formula for the bond calculator. Results will be calculated based on the info provided by the user and displayed.
    print("")
    print (f"For a house worth £{house}, at {rate}% interest rate, you would have to repay £{round(repayment,2)} per month for {months} months")

