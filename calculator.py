"""
This program is all about making a simple calculator(not a GUI calculator).
We can do all simple operations like addition,subtraction,multiplication,division.
"""
a="add"             # First of all defined all the operation
s="sub"
m="mul"
d="div"
num1=int(input("Enter number 1:"))  # Take number1 from user in form of integer
num2=int(input("Enter number 2:"))  # Take number2 from user in form of integer
operation=input("Enter the operation you want to perform(add,sub,mul,div)") # Takes the type of operation that user has to perform
if(operation==a):
    print("The sum of two numbers is:",num1+num2)
elif(operation==s):
    print("The subtraction of two numbers is:",num1-num2)
elif(operation==m):
    print("The multiplication of two numbers is:",num1*num2)
elif(operation==d):
    print("The division of two numbers is:",num1%num2)

# Code by Shubham Sharma , Freelancer Developer
    
