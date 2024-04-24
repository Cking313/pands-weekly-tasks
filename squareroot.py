# squareroot.py
# A function to calculate the square root of a number
# Author: Colleen King
# math library used for testing to compare my sqrt to math.sqrt
# import math

# newton's method
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
def sqrt(n):
    x = n
 
    while True :
        root = 0.5 * (x + (n / x)) 

        # if the root is very close to x then finish
        if (abs(root - x) < 0.0001) :
            break
        x = root
    return root

# print((sqrt(3), math.sqrt(3)))
# print((sqrt(16), math.sqrt(16)))
# print((sqrt(543), math.sqrt(543)))

input = float(input('Please enter a positive number: \n'))
print(f"The square root of {input} is approx. {sqrt(input)}")