#day5
lst = []
lst1 = ["samin", 'lashgari', 22, {'job' : "developer"}, (1, 2, 3) ]
length = len(lst1)
print(lst1[0])
print(lst1[int(length/2)])
print(lst1[-1])
mixed_data_types = ["samin", 22, 164, 'single', 'tehran,takestan']
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'Oracle', 'amazon']
print(it_companies)
print(len(it_companies))
print(f'first one is {it_companies[0]} the middle one is {it_companies[int(len(it_companies)/2)]} and the last one is {it_companies[-1]}')
it_companies[4] = 'samsung'
it_companies.append("isc")
print(it_companies)
it_companies.insert(int(len(it_companies) / 2), 'mositto')
print(it_companies)
it_companies[0] = "ibm".upper()
print(it_companies)
print('#'.join(it_companies))
print("IBM" in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])

it_companies.pop(0)
print(it_companies)
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(min(ages))
print(ages)
