dog = {}

dog_dict = {
    'name': 'Tom',
    'color': 'white',
    'breed': 'Greyhound',
    'legs': 4,
    'age': 2
}

print(dog_dict)

student_dict = {
    'first_name': 'Anurag',
    'last_name': 'Mukherjee',
    'gender': 'Male',
    'age': 19,
    'Martial_status': False,
    'skills': ['Python', 'JavaScript', 'HTML5', 'CSS3', 'MySQL'],
    'country': 'India',
    'city': 'Chandannagar',
    'address':{
        'street':'Kalitola lane, Fatokgora',
        'zipcode':'712136'
    }
}

print(len(student_dict))

print(type(student_dict.get('skills')))

student_dict['skills'].append('Java, CPP')
print(student_dict.get('skills'))

print(student_dict.keys())

print(student_dict.values())

items_student_dict = student_dict.items()
print(items_student_dict)

student_dict.popitem()
print(student_dict)

del dog_dict