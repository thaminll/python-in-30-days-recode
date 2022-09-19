# sets
from this import s


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add('Twitter')
it_companies.update(['isc', 'snapp', 'digikala'])
print(it_companies)
it_companies.remove('digikala')
print(it_companies)

#remove returns error if the set doesnt have the item but discard wont

c = A.union(B)
print(c)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

del A
del B
del c

ages = set(age)
print(len(age))
print(len(ages))

sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split(' '))
print(len(words))
