numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
x = [i for i in numbers if i < 1]
print(x)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
nums = [number for row in list_of_lists for item in row for number in item]
print(nums)

tup = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(10)]
print(tup)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
coun = [(item[0].upper(), item[0][:3].upper(), item[1]) for row in countries for item in row]
print(coun)

dic = [{'country' : item[0], 'city' : item[1]} for row in countries for item in row]
print(dic)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name = [(item[0] + ' ' + item[1]) for row in names for item in row]
print(name)

slope = lambda y2, y1, x2, x1 : (y2 - y1) / (x2 - x1)
print(slope(5, 1, 3, 1))