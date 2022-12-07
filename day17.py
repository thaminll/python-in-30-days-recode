try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

dict = {"name" : "Asabeneh", "country" : "Finland", "city" : "Helsinki", "age" : 250}

def packing_person_info(**dict):
    for key in dict:
        print(f"{key} = {dict[key]}")
    return dict

print(packing_person_info(**dict))

for index, i in enumerate([20, 30, 40]):
    print(index, i)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit" : f, "veg" : v})
print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries , es, ru = names
print(nordic_countries, es, ru)