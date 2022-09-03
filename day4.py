#day4


sentence = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(sentence))

sent = ['Coding', 'For', 'All']
print(' '.join(sent))

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])

print(company.index("Coding"))
print(company.find("Coding"))

print(company.replace("Coding", "Python"))

print(company.split(' '))

com = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(com.split(','))

print(company[0])
print(company[-1])
print(company[10])

acr = company.split(' ')
acrr = ''
for i in acr:
    acrr += i[0]
print(acrr)

sen = '   Coding For All      '
print(sen.strip(' '))

print('30DaysOfPython'.isidentifier())

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(lib))

jomle = "I am enjoying this challenge.\nI just wonder what is next."
print(jomle)









