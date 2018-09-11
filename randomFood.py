#I can't decide what food I want
#So I want to make a program to randomize my food choices
#How original

import random

food_list = []
food_list.append(input("What are you in the mood for? "))

for item in food_list:
    if 'GO' in food_list:
        food_list.remove('GO')
        print(food_list, random.choice(food_list))
    elif len(food_list) >= 2:
        print(food_list)
        food_list.append(input("What else? Type 'GO' to run: "))
    else:
        print(food_list)
        food_list.append(input("What else? "))
