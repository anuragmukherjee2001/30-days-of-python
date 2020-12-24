import re

def is_valid_variable(string):
    valied_str = '^[A-Za-z_][A-Za-z0-9_]*'

    if(re.search(valied_str, string) and '-' not in string):
        return True
    else:
        return False


print(is_valid_variable('first_name')) 
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))            