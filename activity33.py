def add (a, b):
    return a+b
def subtract (a, b):
    return a-b
def multiply (a, b):
    return a*b
def divide (a, b):
    return a/b

print ("chose 1 option:")
print ("a. add")
print ("b. subtract")
print ("c. multiply")
print ("d. divide")

choice=input("enter your choice: ")
num1=int(input("enter first number:"))
num2=int(input("enter second number: "))
if (choice == 'a'):
    print ("result is ", add(num1, num2))
elif (choice == 'b'):
    print ("result is ", subtract(num1, num2))
elif (choice == 'c'):
    print ("result is ", multiply(num1, num2))
elif (choice == 'd'):
    print ("result is ", divide(num1, num2))
else:
    print ("wrong input")