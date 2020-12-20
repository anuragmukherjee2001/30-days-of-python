countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_char(ele):
    if len(ele) == 6:
        return True
    else:
        return False

res = filter(six_char, countries)
print(list(res))            