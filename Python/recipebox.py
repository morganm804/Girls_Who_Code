import time
date = time.strftime("%d/%m/%Y")
basics ={'Name':'Birthday Cake','Date':date, 'Author':'Lauren Miller', 'Link':'https://imlauramiller.com/birthdaycake/'}
ingredients=['2 C soaked cashews', '1 C almond milk', '1 C coconut nectar', '1 tsp vanilla extract','2 C cocoa powder', '3 C almond flour','1 tsp salt']
instructions=['Blend wet ingredients.','Add dry ingredients to a large mixing bowl and whisk.','Add wet ingredients to dry and mix, no lumps.','Transfer to a parchment-lined tray and smooth out with an offset spatula.','Dehydrate 4 to 5 hours.']
mousseingredients=['2 C soaked cashews','1 C coconut meat','1 C raspberries','1 TBSP vanilla extract','1/4 t salt','1 C coconut nectar','¼ C water','***BLEND*** then add:','1 1/2 C coconut oil, melted']
mousseinstructions=['Blend all ingredients except coconut oil. Add coconut oil into the blender slowly while the blender is running.','Put in a tupperware and in fridge for 4+ hours to set up.']
def user():
    user_input= input('Would you like the ingredients for the cake, mousse or both?:')
    if user_input=='cake':
        for i in range(0, len(ingredients)-1):
            print(ingredients[i]);
        for p in range(0,len(instructions)-1):
            print(instructions[p]);
    if user_input=='mousse':
        for q in range(0,len(mousseingredients)-1):
            print(mousseingredients[q]);
        for m in range(0, len(mousseinstructions)-1):
            print(mousseinstructions[m]);
    if user_input=='both':
        print('Cake:');
        for i in range(0, len(ingredients)-1):
             print(ingredients[i]);
        for p in range(0,len(instructions)-1):
             print(instructions[p]);
        print('Mousse:');
        for q in range(0,len(mousseingredients)-1):
            print(mousseingredients[q]);
        for m in range(0, len(mousseinstructions)-1):
            print(mousseinstructions[m]);
    # else:
    #     print("That's not a valid answer!");
    #     user();

print(basics['Name']);
print(basics['Date']);
print(basics['Author']);
print(basics['Link']);
user()
