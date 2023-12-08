# 10. Write a program to input a 2 digit integer, call it x, where the rightmost digit is non zero. Compute the integer y which has the same digits as x, but in reverse order. Print 
# out x, y and x+y.
# For example:
# Please enter a two digit integer: 23
# 23 reversed is: 32
# 23 + 32 is 55
x=int(input("Please enter a two digit integer:"))
y=int(str(x)[::-1])
s=x+y
print(x," reversed is: ",y)
print(x,"+",y,"=",s)