print("30 " + "Days " + "Of " + "Python ")

print("Coding " + "For " + "All ")

company = "Coding For All"

print(company)

print(len(company))

upper_company = company.upper()
print(upper_company)

lower_company = company.lower()
print(lower_company)

capitalise_company = company.capitalize()
title_company = company.title()
swapcase_company = company.swapcase()

print(capitalise_company)
print(title_company)
print(swapcase_company)

slice_company = slice(0, 6)
print(company[slice_company])

if(company.find('Coding') != -1):
    print("Found")
else:
    print("Not Found")   

replace_company = company.replace("Coding", "Python")
print(replace_company) 

str1 = "Python for Everyone"
replace_str1 = str1.replace("Everyone", "All")
print(replace_str1)

split_company = company.split()
print(split_company)

tech_giants = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_giants.split(","))

char_at_index = company.index(company)
print(company[char_at_index])

print(company[char_at_index -1])

print(company[char_at_index + 10])

str2 = 'Python For Everyone'
str2_split = str2.split()
acronym = ""
for i in  str2_split:
    acronym = acronym +  str(i[0])

print(acronym)

str3 = 'Coding For All'
str3_split = str3.split()
acronym = ""
for i in  str3_split:
    acronym = acronym +  str(i[0])

print(acronym)

sub1_str3 = "C"
sub2_str3 = "F"

print(str3.index(sub1_str3))
print(str3.index(sub2_str3))

str4 = "Coding For All People"
sub_str4 = "i"
print(str4.rfind(sub_str4))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

print(sentence.rindex("because"))

slice_sentence = slice(31, 54)
print(sentence[slice_sentence])

print(str3.startswith('Coding'))
print(str3.endswith('Coding'))

string_with_space = '   Coding For All      '
print(string_with_space.strip())

q_31_str1 = "30DaysOfPython"
q_31_str2 = "thirty_days_of_python"

print(q_31_str1.isidentifier())
print(q_31_str2.isidentifier())

lst1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_list = "# ".join(lst1)
print(joined_list)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\nAsabeneh\t250\tFinland")

radius = 10
area = 3.14 * radius ** 2

print("The area of a cricle with radius", radius ,"is", int(area), "meters square.")

print("8 + 6 = ", 8 + 6)
print("8 - 6 = ", 8 - 6)
print("8 * 6 = ", 8 * 6)
print("8 / 6 = ", 8 / 6)
print("8 % 6 = ", 8 % 6)
print("8 // 6 = ", 8 // 6)
print("8 ** 6 = ", 8 ** 6)