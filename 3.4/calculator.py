#!/usr/bin/python3
""" Simple calculator. """

def adder(num1,num2):
    result = num1 + num2
    return result

def subtractor(num,num2):
    result = num1 - num2
    return result

def multiplier(num1,num2):
    result = num1 * num2
    return result

def divider(num1,num2):
    result = num1 / num2
    return result

def exit_calc():
    res = input("\nExit (y/n)? ")
    if res == "y":
        return 1
    else:
        return 0
try:
    calc = 0
    while calc == 0:
        print("\n[Calculator]\n")
        oper = input("Operation ['+','-','*','/']: ")
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        if oper == "+":
            result = adder(num1,num2)
            print("\n> Result: {0}".format(result))
            calc = exit_calc()
        elif oper == "-":
            result = subtractor(num1,num2)
            print("\n> Result: {0}".format(result))
            calc = exit_calc()
        elif oper == "*":
            result = multiplier(num1,num2)
            print("\n> Result: {0}".format(result))
            calc = exit_calc()
        elif oper == "/":
            result = divider(num1,num2)
            print("\n> Result: {0}".format(result))
            calc = exit_calc()
        else:
            print("Wrong Operator!")
    print("\nBye!\n")
except KeyboardInterrupt as e:
    print("\nInterrupted!\n")

