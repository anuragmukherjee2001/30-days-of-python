countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def new_list(ele):
    if 'land' in ele:
        return True
    else:
        return False

res = filter(new_list, countries)
print(list(res))            