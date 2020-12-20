countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def to_upper(ele):
    return ele.upper()

def contains_land(ele):
    if 'land' in ele:
        return True
    else:
        return False


res = countries.map(to_upper).filter(contains_land)


# this method is giving some error