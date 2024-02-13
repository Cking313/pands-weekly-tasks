#accounts.py 
#Basic account number input and output system  
#Author: Colleen King
# Read account number from user prompt
Account_no = (input("enter account number"))
#Im going to make this a string 
Account_no = str(Account_no)
#format so only the last 4 didgits show using negative slicing 
#https://stackoverflow.com/questions/493046/i-dont-understand-slicing-with-negative-bounds-in-python-how-is-this-supposed
#If Using a negative number as an index in python returns the nth element from the right-hand side of the list (as opposed to the usual left-hand side).
print (Account_no[-4:])
#but that doesnt meet the breif lets mask those numbers with X's
# https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python
print ("*" *6+(Account_no[-4:]))
#make this work for any lenght of card number by removing the 6 and making the number of stars n-4
print ("*" *(len(Account_no)-4) + Account_no[-4:])
#assuming the number is at least four didgits long 
#


