person = {'first_name' : 'Thamin', 'last_name' : 'Lashgari', 'age' : 23, 'major' : 'computer enginering', 'married' : False,
'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }}
print(len(person))
print(person["major"])
#print(person["ages"])
print(person.get('age'))
person['job_experience'] = 2
person['skills'].append('linux')
print(person)

print('skills' in person)

print(person.pop('last_name'))
person.popitem()
del person["age"]
print(person)

print(person.items())
print(person.keys())
print(person.values())


print(type(person['skills']))
person['skills'].append('network')
print(person.values())
print(person.items())
person.pop('major')
del person