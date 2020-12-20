countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def start_eith_E(ele):
    if ele.startswith('E'):
        return True
    else:
        return(False)

res = filter(start_eith_E, countries)
print(list(res))            