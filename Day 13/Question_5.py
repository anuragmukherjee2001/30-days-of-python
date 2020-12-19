def lst_to_dict(lstA, lstB):
    zipped = zip(lstA, lstB)
    dict_lst = dict(zipped)
    return dict_lst

def merge_dict(dictA, dictB):
    res = {**dictA, **dictB}
    return res   

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

two_dimentional = [number for row in countries for number in row]
one_dimentional = [number for row in two_dimentional for number in row]

lst_countries1 = [one_dimentional[0]]
lst_countries2 = [one_dimentional[2]]
lst_countries3 = [one_dimentional[4]]

city1 = [one_dimentional[1]]
city2 = [one_dimentional[3]]
city3 = [one_dimentional[5]]

lst_coun = ['countries']
lst_city = ['city']

dict_country1 = lst_to_dict(lst_coun, lst_countries1)
dict_country2 = lst_to_dict(lst_coun, lst_countries2)
dict_country3 = lst_to_dict(lst_coun, lst_countries3)

dict_city1 = lst_to_dict(lst_city, city1)
dict_city2 = lst_to_dict(lst_city, city2)
dict_city3 = lst_to_dict(lst_city, city3)

var1 = merge_dict(dict_country1, dict_city1)
var2 = merge_dict(dict_country2, dict_city2)
var3 = merge_dict(dict_country3, dict_city3)

lst_merged = [var1, var2, var3]
print(lst_merged)