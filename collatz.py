# collatz.py
# Prints numbers of collatz procedure for an input
# Author: Colleen King
# take a number from the user and parse as integer
input = int(input("Input a number:\n"))
# keep going until the number is 1
while input != 1:
    # check remainder modulo 2 for evenness - 0 means divisible by 2
    if input % 2 == 0:
        # divide by 2 if even - //= for integer division so the value isn't cast to a float
        input = input // 2
        print(input)
    else:
        # if number is not even, then it's odd
        input = input*3 +1
        print(input)
