# def convert_celsius_to_fahrenheit():
#     c = int(input("enter the c:"))
#     f = (c * 9.5) + 32
#     return(f)

# print(convert_celsius_to_fahrenheit())

# def reverse_list():
#     lst = []
#     num = int(input("enter the number of the list:"))
#     for i in range(num):
#         item = input("enter:")
#         lst.append(item)
#     print(lst)
#     print(lst[::-1])

# reverse_list()

# def capitalize_list_items():
#     lst = []
#     num = int(input("enter the number of the list:"))
#     for i in range(num):
#         item = input("enter:")
#         lst.append(item)
#     print(lst)
#     lst1 = []
#     for item in lst:
#         lst1.append(item.upper())
#     print(lst1)
# capitalize_list_items()

# nameList = ['hello', 'samin', 'boo', 'bye']
# def remove_item():
#     rem = input("enter what to ewmove:")
#     for item in nameList:
#         if item == rem:
#             nameList.remove(item)
#     print(nameList)

# remove_item()

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)
    
print(factorial(5))

def is_empty(lst):
    if len(lst) == 0:
        print("is empty")
    else:
        print("its not empty")

is_empty([1,2])

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def uniqe(list):
    if len(list) == len(set(list)):
        return True
    else: 
        return False
print(uniqe([1, 2, 5, 1]))

def same_dataType(lst):
    typee = type(lst[0])
    for item in lst:
        if type(item) == typee:
            result = True
            continue
        else:
            result = False
            break
            
    if result:
        print("all the same")
    else:
        print("not the same:")

same_dataType([1, 2, 3, "s"])

def valid_var(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(valid_var('tam'))

def most_spoken(countries_info):
    lang_counter ={}
    for item in countries_info:
        for lang in item["languages"]:
            if lang in lang_counter:
                lang_counter[lang] += 1
            else:
                lang_counter[lang] = 1

    pop = sorted(lang_counter, key=lang_counter.get, reverse=True)
    top_20 = pop[:20]
    print(top_20)

def most_populated(countries_info):
    populated = []
    for item in countries_info:
        populated.append(item['population'])
    
    pop = sorted(populated, reverse=True)

    most_20 = []
    for i in populated:
        for item in countries_info:
            if i == item['population']:
                most_20.append(item['name'])

    print(most_20[:20])

    
