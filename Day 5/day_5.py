lst1 = []

list2 = [1, 2, 3, 5, 9]

print(len(list2))

mid = (0 + len(list2) - 1)//2

print(list2[0]) 
print(list2[len(list2) - 1])
print(list2[mid])

mixed_data_types = ['Anurag', 19, 5.8, False, 'Chandannagar, hooghly, West Bengal India']

it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print("The number of companies in the list is", len(it_companies))

print("The first company is ", it_companies[0])
print("The middle company is ", it_companies[(0 + len(it_companies) - 1)//2])
print("The last company in the list is ", it_companies[len(it_companies) - 1])

it_companies[3] = 'Netflix'
print(it_companies)

it_companies.append('Samsung')
print(it_companies)

mid = ((len(it_companies) - 1)//2)

it_companies.insert(mid, 'Alphabet')
print(it_companies)

modified_it_companies = it_companies[1].upper()
print(modified_it_companies)

joined_company = '#;'.join(it_companies) 
print(joined_company)

if 'Amazon' in it_companies:
    print('True')
else:
    print("False")    

it_companies.sort()
print(it_companies)

print(list(reversed(it_companies)))  

print(it_companies[0:3])

print(it_companies[len(it_companies)-3:len(it_companies)])

print(it_companies[((len(it_companies) - 1)//2):((len(it_companies) - 1)//2) + 1])

del it_companies[0]
print(it_companies)

del it_companies[((len(it_companies) - 1)//2)]
print(it_companies)

del it_companies[(len(it_companies) - 1)]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)

full_stack = joined_list.copy()
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages[0])
print(ages[len(ages) - 1])

ages.append(min(ages))
ages.append(max(ages))
print(ages)

length_of_the_list = len(ages)

if length_of_the_list % 2 == 0:
    median = (ages[((len(ages) - 1)//2)] + ages[((len(ages) - 1)//2) + 1]) / 2
else:
    median = (ages[((len(ages) - 1)//2)]) / 2   

print(median)    

sum_of_all_elements_in_the_list = sum(ages)
print((sum_of_all_elements_in_the_list) / len(ages))

min_age = min(ages)
max_age = max(ages)
range = max_age - min_age
print(range)

average = sum_of_all_elements_in_the_list / len(ages)
print(abs(min_age - average))
print(abs(max_age - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print("The middle country is ", countries[len(countries)//2])

first_half_countries = countries[0:len(countries)//2 + 1]
print(first_half_countries)
second_half_countries = countries[len(countries)//2:len(countries) - 1]
print(second_half_countries)

country_list_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
unpacking_the_first_3 = [country_list_2[0], country_list_2[1], country_list_2[2]]
print(unpacking_the_first_3)