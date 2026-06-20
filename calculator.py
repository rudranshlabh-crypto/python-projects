n1 = float(input("Number 1: "))
op = input("Operation: ")
n2 = float(input("Number 2: "))

if op == '+': print("Result:", n1 + n2)
elif op == '-': print("Result:", n1 - n2)
elif op == '*': print("Result:", n1 * n2)
elif op == '/': print("Result:", n1 / n2)
else: print("Invalid operation")