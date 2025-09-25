import re

def check_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(pattern, password):
        return 
    else:
        return 
password = input("Enter your password: ")
print(check_password(password))

