from string import *
import random

char = ascii_letters + digits
user_id = ''
for i in range(6):
    ch = random.choice(char)
    user_id += ch
print(user_id)

def user_id_gen_by_user(num_id, num_char):
    char = ascii_letters + digits
    
    for i in range(num_id):
        user_id = ''
        for i in range(num_char):
            ch = random.choice(char)
            user_id += ch
        print(user_id)
user_id_gen_by_user(3, 5)

def shuffle_list(list):
    shuffled_list = []
    while len(list) > 0:
        rand = list[random.randint(0, len(list) - 1)]
        shuffled_list.append(rand)
        list.remove(rand)
    print(shuffled_list)

shuffle_list(["salam", 'jojo', 'khob', 'nice'])

def seven_random():
    list_seven = []
    while len(list_seven) != 7 :
        rand_num = random.randint(0, 9)
        if rand_num in list_seven:
            continue
        else:
            list_seven.append(rand_num)
    print(list_seven)
seven_random()