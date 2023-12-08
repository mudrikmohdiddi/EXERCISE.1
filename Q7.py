# 7. Write a program to ask the user for a three digit integer (the rightmost digit should not 
# be 0). Print the original number and the print the digits in reverse order. For example:
# Please enter a three digit integer: 123
# You entered: 123
# 123 reversed is 321.
a=int(input("Please enter a three digit integer:"))
print("You entered:",a)
r=int(str(a)[::-1])
print(a,"reversed is ",r)
