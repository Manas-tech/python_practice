a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
c=a+b
print("The sum of the numbers entered is {0:>5} ".format(c)) #right format
c=a-b
print("The difference of the numbers entered is {0:<2} ".format(c))  #left format
c=a*b
print("The multiplication of the numbers entered is {0:^5} ".format(c))  #center format
c=a/b
print("The division of the numbers entered is {} ".format(c))
c=a%b
print("The modulus of the numbers entered is {} ".format(c))