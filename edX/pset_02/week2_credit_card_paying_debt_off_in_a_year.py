"""                                                                             
 Exam from Week 2 (MITx: 6.00.1x):                                              
      Introduction to Computer Science and Programming Using Python
"""

balance = 3329 ###
annualInterestRate = 0.2 ###
monthlyInterestRate = annualInterestRate / 12.0

prev_balance = balance
minimum_payment = 10

oper = 1 ###

while True:
    
    print("\nOperation:", oper) ###
    #print("Interest:", monthlyInterestRate)
    for m in range(1, 13):
        print("\n- month:", m) ###
        print("- current balance:", prev_balance) ###
        unpaid_balance = prev_balance - minimum_payment
        print("- unpaid balance: ", unpaid_balance) ###
        prev_balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)
        print("- new balance (w/ interest):", prev_balance) ###

    print("\nFinal balance:   ", prev_balance) ###
    print("Miminum payment: ", minimum_payment) ###
    input()
    if prev_balance <= 0:
        print("\nLowest Payment:", minimum_payment)
        break
    else:
        prev_balance = balance
        minimum_payment += 10

    oper += 1 ###
