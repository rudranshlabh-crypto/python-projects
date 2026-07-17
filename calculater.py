ef add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "Error: Division by zero" if b == 0 else a / b

def get_num(prompt):
    while True:
        try: return float(input(prompt))
        except ValueError: print("Invalid number.")

while True:
    print("\n1. Add | 2. Sub | 3. Mul | 4. Div | 5. Exit")
    choice = input("Pick operation (1-5): ")
    
    if choice == '5': 
        break
        
    if choice in ['1', '2', '3', '4']:
        n1 = get_num("First number: ")
        n2 = get_num("Second number: ")
        
        if choice == '1': print("Result:", add(n1, n2))
        if choice == '2': print("Result:", sub(n1, n2))
        if choice == '3': print("Result:", mul(n1, n2))
        if choice == '4': print("Result:", div(n1, n2))
    else:
        print("Invalid choice.")