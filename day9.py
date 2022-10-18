a = 2
b = 3

print('number two') if a == 2 else print("another number")
if a > 1:
    if b > 1:
        print(a * b)

if a > 1  and b > 1:
    print(a * b)

age = int(input("please enter the age: "))
if age > 18 :
    print("you are old enough ti learn to drive")
else:
    print(f'you need {18 - age} more years to learn to drive')


grade = int(input("enter your grade: "))
if grade >= 80:
    print("A")
elif grade >= 70 and grade <80:
    print("B")
elif grade >=60 and grade < 70:
    print("C")
else:
    print("D")

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
print(len(person["skills"]))
if 'skills' in person:
    print(f'{person["skills"][int(len(person["skills"]) / 2) ]}')

if 'skills' in person:
    if 'Python' in person['skills']:
        print("yeeees the person is a python programmer")
    else:
        print("NO")

if ('JavaScript' and 'React') in person['skills'] and len(person['skills']) == 2:
        print('He is a front end developer')
elif ('Node' and 'MongoDB' and 'Python') in person['skills'] and len(person['skills']) == 3:
        print('He is a back end developer')
elif ('Node' and 'MongoDB' and 'React') in person['skills'] and len(person['skills']) == 3:
        print('He is a full stack developer')
else:
    print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]} ')