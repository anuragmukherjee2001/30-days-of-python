countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def to_upper(country):
    return country.upper()

res = map(to_upper,countries)
print(list(res))    