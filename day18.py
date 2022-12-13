import re, random

txt = 'I love to teach python and javaScript'

match = re.match("I love to teach", txt, re.I)
print(match)  

span = match.span()
print(span)     

start, end = span
print(start, end)  

substring = txt[start:end]
print(substring)       

txts = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matche = re.match('lannguage', txts, re.I)
print(matche)
matchee = re.search('language', txts, re.I)
print(matchee)
span = matchee.span()
print(span)
print(re.findall('python', txts))
print(re.findall('python', txts, re.I))
print(re.findall('python|Python', txts))

#Let us add one more example. The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text.

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

print(re.sub('%', '', txt))

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol

text = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
regex_pattern = r'[Aa]pple'
print(re.findall(regex_pattern, text))

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''


words = paragraph.split()

print(words)
dict = {}
for item in words:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)
print(sorted(dict.items(), key=lambda kv:
                 (kv[1], kv[0]), reverse=True))
 
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'

match = re.findall('[-+]?\d+', text)
print(match)

x = int(random.choice(match))
y = int(random.choice(match))
m = y - x
print(x, y, m)

def is_identifier(str):
    regex = '^[A-Za-z_!@#$%^&*()-+=][A-Za-z0-9_]*'
    if(re.search(regex, str)):
        print("Valid Identifier")
         
    else:
        print("Invalid Identifier")
    
is_identifier('1first_name')
is_identifier('first_name')

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sen1 = re.sub('%|@|&|$|#|','', sentence)
print(sen1)

words = sen1.split()
dict = {}
for item in words:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
freq = sorted(dict.items(), key = lambda kv : (kv[1], kv[0]) , reverse=True)
top_3 = freq[:3]
print(freq)
print(top_3)