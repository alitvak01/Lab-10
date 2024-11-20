red_velvet = {"cake flour": 3, "baking soda":1, "cocao powder":2, "salt":1.5, "butter":1.5, "sugar":2, "oil":1, "eggs":4, "vanilla extract":1, "vinegar":1, "red dye":1, "buttermilk":1}
lemon_cake = {"lemon":2, "flour":1.5, "egg":2, "sugar":1, "baking powder":2, "salt":0.5, "butter":0.5, "vanilla extract":1.5, "milk":0.5}

def cake_recipes(dict1, dict2):
    for key in dict1:
        if key in dict2:
            print (key)


cake_recipes(red_velvet, lemon_cake)
