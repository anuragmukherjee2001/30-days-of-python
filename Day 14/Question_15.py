number_str = ['My', 'Name', 5, 6, 'is', 'Anurag', 7, 1000]


def get_string_lists(ele):
    if type(ele) == str:
        return ele
    else:
        pass    

res = map(get_string_lists, number_str)
print(list(res))


