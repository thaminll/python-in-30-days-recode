from functools import *

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

country = map(lambda countrie : countrie.upper(), countries)
print(list(country))

squ = map(lambda num : num **2, numbers)
print(list(squ))

def land(cou):
    if "land" in cou:
        return True
    else:
        return False

landcou = filter(land, countries)
print(list(landcou))

def char(coun):
    if len(coun) == 6:
        return True
    else:
        return False

char6 = filter(char, countries)
print(list(char6))

def starE(couunt):
    if couunt[0] == 'E':
        return True
    else:
        return False

startE = filter(starE, countries)
print(list(startE))

def get_string_lists(item):
    return str(item)

stritem = map(get_string_lists, numbers)
print(list(stritem))

sumnum = reduce(lambda x, y: x + y, numbers)
print(sumnum)

# sent = reduce(lambda f'{x}, {y, }' , y : x + y , countries)
# print(sent)
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries


