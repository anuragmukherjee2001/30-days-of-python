import random
import string

def user_id_gen_by_user():
    n = int(input("Enter the number of characters: "))
    num_id = int(input("Enter the number of ids to be generated: "))
    generate_id(n, num_id)

def generate_id(n, num_id):
    user_id = string.ascii_letters + string.digits
    for i in range(num_id):
        result_str = ''.join(random.choice(user_id) for i in range(n)) 
        print(result_str)

user_id_gen_by_user()           