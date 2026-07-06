import math

while True:
    area = float(input("Enter circle area (or 0 to stop): "))
    
    if area == 0:
        print ("Goodbye!")
        break

       combined_number = 4 * 3.14 * area
    circumference = combined_number ** 0.5
    
    print ("The circumference is:", circumference)