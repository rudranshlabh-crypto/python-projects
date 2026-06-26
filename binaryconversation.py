string = input ("enter your own number:")
decimal_result = 0
length = len(string)

for i in range(length):
    digit = int(string[i])
    
    if digit == 1:
        power = length - 1 - i
        
        power_value = 1
        for j in range(power):
            power_value = power_value * 2
        
        decimal_result = decimal_result + power_value

print("Your binary number is:")
print(decimal_result)