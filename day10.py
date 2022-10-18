import countries
import countries_data

number = 0
while number < 10:
    print(number)
    number +=1
else:
    print(f'the loop stops at {number}')

for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)


for i in range(1, 8):
    print("#" * i)

for i in range(9):
        print("#" * 9)

for i in range(0, 11):
    print(f'{i} x {i} = {i * i}')

for i in range(100):
    if i % 2 == 0:
        print(i)

sum = 0
for i in range(101):
    sum += i
print(sum)

for country in countries.countries:
    if 'land' in country:
        print(country)

fruits =  ['banana', 'orange', 'mango', 'lemon']
for item in range(len(fruits) - 1, -1, -1):
    print(fruits[item])

language = []
for item in countries_data.data:
    for lan in item['languages']:
        language.append(lan)

lang = set(language)
print(len(lang))

lang_counter = {}
for item in countries_data.data:
    for lang in item['languages']: 
        if lang in lang_counter:
            lang_counter[lang] += 1
        else:
            lang_counter[lang] = 1
popular_langs = sorted(lang_counter, key = lang_counter.get, reverse = True) 
top_10 = popular_langs[:10]
print(top_10)


population = []
for item in countries_data.data:
    population.append(item['population'])
 
most_pop = sorted(population, reverse = True) 
top_10 = most_pop[:10]
print(top_10)

most_10 = []
for i in top_10:
    for item in countries_data.data:
        if i == item["population"]:
            most_10.append(item['name'])

print(most_10)