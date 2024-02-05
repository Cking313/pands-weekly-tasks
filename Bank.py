#Bank.py 
#Basic banking system 
#Author: Colleen King
# Read two numbers from user prompt 
amount_A = int(input("enter amount: in cent no decimal \n"))
amount_B = int(input("enter amount: in cent no decimal \n"))

# convert cents to euros
total = (amount_A+amount_B)/100

#Format the price to 2 decimal places
# https://www.w3schools.com/python/ref_string_format.asp
txt = "the sum of these is €{price:.2f}"
print(txt.format(price = total))
