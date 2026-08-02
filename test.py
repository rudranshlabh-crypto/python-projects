import random
import string

def generate_random_password(length=12):
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    
    all_characters = string.ascii_letters + string.digits
    
    remaining_length = length - 3
    remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]
    
    password_list = [lower, upper, digit] + remaining_chars
    n
    random.shuffle(password_list)
    
    return "".join(password_list)

print("Generated Password:", generate_random_password(12))