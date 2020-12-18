import random
import string

def random_user_id():
    user_id = string.ascii_letters + string.digits 
    result_str = ''.join(random.choice(user_id) for i in range(6))
    return result_str

print(random_user_id())    