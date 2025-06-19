import re

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[@#$%^&+=]", password)

    if all([length, upper, lower, digit, special]):
        return "Strong"
    return "Weak"

password=input("Password")
print(check_password_strength(password)) 
