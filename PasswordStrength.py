import re

def check_password_strength(password):
    # At least 8 characters
    length_error = len(password) < 8
    # At least one digit
    digit_error = re.search(r"\d", password) is None
    # At least one uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None
    # At least one lowercase
    lowercase_error = re.search(r"[a-z]", password) is None
    # At least one special character
    symbol_error = re.search(r"[@$!%*?&]", password) is None

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        return "Strong Password ✅"
    else:
        return "Weak Password ❌"

# Example
password = input("Enter a password: ")
print(check_password_strength(password))