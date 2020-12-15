person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    lst = person['skills']
    length = len(person['skills'])
    print(lst[length//2])
else:
    print("The person has no skills key") 

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python is present")
    else:
        print("Python is not present")    
else:
    print("The person has no skills key")      

if 'skills' in person:

    frontend = ['JavaScript', 'React']
    backend = ['Node', 'Python', 'MongoDB']
    fullStack = ['React', 'Node','MongoDB','JavaScript','Python']
    
    if person['skills'] == frontend:
        print("He is a front end developer")
    elif person['skills'] == backend:
        print('He is a backend developer')
    elif person['skills'] == fullStack:
        print("He is a full stack developer")
    else:
        print('unknown title')           
else:
    print("The person has no skills key")  

if person['is_marred'] == True and person['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in", person['country'],". He is married.")
