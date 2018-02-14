#!/usr/bin/python3

# my secret number
secret = 42

# limits 
high = 100
low  = 0

print("\nPlease think of a number between 0 and 100!")

loop = True
while loop == True:
    # calculates a guess for every loop step...
    ans = (high + low) // 2
    print("\nLow ({0}) + High ({1}) // 2 == {2}".format(low,high,ans))
    print("Is your secret number {0}?".format(ans))
    print("Enter 'h' to indicate the guess is too high.") 
    print("Enter 'l' to indicate the guess is too low.")
    print("Enter 'c' to indicate I guessed correctly.")
    opt = input()
    if opt == "h":
        # if too high, the high limit is reduced
        high = ans
    elif opt == "l":
        # if too low, the low limit is increased 
        low = ans
    elif opt == "c":
        print("\nGame over. Your secret number is: {0}".format(int(ans)))
        loop = False
    else:
        print("Sorry, I did not understand your input.")
 
