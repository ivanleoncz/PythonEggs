#!/usr/bin/python3
"""
 Exam from Week 2 (MITx: 6.00.1x): 
 Introduction to Computer Science and Programming Using Python

 INFO:
 - When submitting the exercise, remove the lines that contains '###'
 (variables and prints).                                                         

 PROBLEM
 - Write a program to calculate the credit card balance 
 after one year if a person only pays the minimum monthly payment
 required by the credit card company each month.

 FLOW
 - For each month, calculate statements on the monthly payment and
 remaining balance. At the end of 12 months, print out the remaining
 balance. Be sure to print out no more than two decimal digits of accuracy

 INPUTS
 - balance: the outstanding balance on the credit card
 - annualInterestRate: annual interest rate as a decimal
 - monthlyPaymentRate: minimum monthly payment rate as a decimal

"""

balance = 42 ###
annualInterestRate = 0.2  # annual interest ###
monthlyPaymentRate = 0.04 # % to pay, per month
monthlyInterestRate = annualInterestRate / 12.0  # annual interest, per month

previous_balance = balance

print("\nINITIAL BALANCE:", previous_balance) ###

for m in range(1, 13):
    print("MONTH", m) ###
    minimum_payment  = monthlyPaymentRate * previous_balance
    print(" - minimum payment:", minimum_payment) ###
    unpaid_balance   = previous_balance - minimum_payment
    print(" - unpaid balance:", unpaid_balance) ###
    # calculating annual interest for the new balance... 
    previous_balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)
    print(" - new balance", previous_balance, "\n") ###

print("Remaining balance: {:.2f}".format(previous_balance))


