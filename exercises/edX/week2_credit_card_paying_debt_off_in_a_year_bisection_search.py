""" 
Exam from Week 2: 
- Introduction to Computer Science and Programming Using Python by EDX

Info:
- When submitting the exercise, remove the lines that contains '###' 
(variables and prints). 
"""

balance = 320000          ###
annualInterestRate = 0.2  ### 
monthlyInterestRate = annualInterestRate / 12.0

prev_balance = balance

lower_bound = 0
upper_bound = balance + ((annualInterestRate * balance) / 100)

oper = 1 ###

while True:
    
    guess = (lower_bound + upper_bound) / 2
    print("Operation:", oper) ###
    print("- lower bound:     ", lower_bound) ###
    print("- upper bound:     ", upper_bound) ###
    print("- guess:           ", guess) ###
    for m in range(1, 13):
        unpaid_balance = prev_balance - guess
        prev_balance = round(unpaid_balance + (monthlyInterestRate * unpaid_balance), 2)
    print("- final balance:   ", prev_balance) ###
    print("- miminum payment: ", guess) ###

    calculation = 12.0 * guess
    if abs(prev_balance) == 0.0:
        print("\nLowest Payment:", round(guess, 2))
        break   
    elif prev_balance > 0:
        print("Positive Balance:", round(calculation, 2)) ###
        prev_balance = balance
        lower_bound = guess
    elif prev_balance < 0:
        print("Negative Balance:", round(calculation, 2)) ###
        prev_balance = balance
        upper_bound = guess

    oper += 1 ###
