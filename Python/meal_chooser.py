import random
#menu options lists
appetizer=["fries","stuffed potatoes","mozzerella sticks"]
main=["shrimp", "pizza", "pasta"]
dessert=["lava cake", "carrot cake", "cookie", "ice cream"]
#defines the function meal
def meal():
    print(main[random.randint(0,2)])
#begin program output
print("The chef will choose your meal tonight, all you have to do is ask")
print('Do you want an appetizer or to go straight to the meal? Type appetizer or meal')
answer1=input()
if answer1=='appetizer':
    print(appetizer[random.randint(0,2)])
    meal()
else:
    meal()
print('Do you want dessert? Type yes or no')
answer2=input()
if answer2=='yes':
    print(dessert[random.randint(0,3)])
    print("We hope you enjoyed your meal!")
else:
    print("Maybe next time... Have a nice night!")
