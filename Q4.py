# 4. Write a program to ask the user to input a floating point number. Your program 
# should print out the integer par and the fractional part separately. For example: 
# Please enter a floating point number: 3.678
# You entered: 3.678
# The integer part is: 3.
# The fractional part is: 678
f=float(input("Please enter a floating point number:"))
print("You entered:",f)
integer=int(f)
fractional=float('.'+str(f).split('.')[1])
print("The integer part is:",integer)
print("The fractional part is:",fractional)
